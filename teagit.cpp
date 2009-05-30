
//
//  A very simple parser that is almost (but not quite) 
//  entirely unlike Git..... :)  
//  Yep, this is Teagit in C++.  
//  
//  NOTE - as of now (30th May 2009) this parser requires 
//  Boost::Spirit version 2.1. At present you will need to 
//  get that version via svn. The following command will check out 
//  Boost-trunk - that will get you this version - 
//  
//  svn co http://svn.boost.org/svn/boost/trunk boost-trunk
//
//  Written by:  Andy Elvey
// 
//  Acknowledgements: I want to acknowledge (and give a huge 
//  "Thank you!" to all of the developers of Boost::Spirit, pretty 
//  much all of whom have helped me at one time or another on the 
//  Spirit mailing-list.     
//  
//  Another very big "thank you" to the developers of Git - the DVCS 
//  that rules the universe. First written by Linus Torvalds and now 
//  maintained by Junio Hamano and a "cast of thousands". 
//  ( Well, "lots" anyway.....  :)  ) 
//    
//  This parser is released to the public domain.  
//    
//  "Share and enjoy......"  :)  
//    
//#define BOOST_SPIRIT_DEBUG  ///$$$ DEFINE THIS WHEN DEBUGGING $$$///


#include <boost/config/warning_disable.hpp>
#include <boost/spirit/include/qi.hpp>

#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace boost::spirit;
using namespace boost::spirit::qi;
using namespace boost::spirit::ascii;
using namespace boost::spirit::qi::labels;


///////////////////////////////////////////////////////////////////////////////
//  Our grammar
///////////////////////////////////////////////////////////////////////////////

//  NOTE - For now, I've just put three commands here, but this gives the 
//  general idea.....  :)   
// 
//  NOTE 2 - I have put the commit command first in the grammar because this 
//  helps in minimising the abiguity of the grammar.  
//  In general, I have found it to be a good idea to put the longest 
//  grammar clauses first in Spirit grammars.   

template <typename Iterator>
struct teagit_grammar : grammar<Iterator, space_type> 
{
    teagit_grammar() : teagit_grammar::base_type(expression)
	
    {
		
    expression 					
	%=  +( commands ) ;  
		
	commands 
	%= git_commit_cmd
	|  git_init_cmd 
	|  git_add_cmd ; 
	
//  The "git commit" command. 
//  Here, we give two versions of the commit command - the long and 
//  the short one. This helps to reduce ambiguity in the grammar. 
    git_commit_cmd 
	%=  long_commit_cmd | short_commit_cmd ; 
	
//  Long version of commit. 
//  This has an optional "-a" for "all".  
	long_commit_cmd 
	%=  lit("git") >> lit("commit") 
	>>  lit("-m") >> sentence; 
		
//  Sentence.  
    sentence 
	%=  lexeme[ lit('"')  
    >>  *( ( print - lit('"') )  | space) 
	>>  lit('"') ];  

//  Short version of commit.  	
	short_commit_cmd 
	%=  lit("git") >> lit("commit") ; 
			
// 	The "git init" command. 
    git_init_cmd 
	%=  lit("git") >> lit("init");  	
		
//  The "git add" command 
    git_add_cmd 
	%=  lit("git") >> lit("add") 
	 >>  lit(".") | files ;
		 					 		 	
//  Files 
    files %= +( identifier ); 
		 			
//  Identifier 	                                           	
    identifier %= lexeme[ ( alpha >> *(alnum | '_' | '.' | '-' ) ) ] ;   					   		               
								   	  							   								                                                                                                                                                                                                                                                                 
   }

      rule<Iterator, space_type> expression, commands, git_init_cmd, 
	     git_add_cmd, git_commit_cmd, long_commit_cmd, short_commit_cmd, 
		 files, identifier, sentence;  		             
							      
};



int main()  
{
    std::cout << "/////////////////////////////////////////////////////////\n\n";
    std::cout << "\t\t A toy Git-like parser...\n\n";
    std::cout << "/////////////////////////////////////////////////////////\n\n";
    std::cout << "Type a Git command  \n" ; 
    std::cout << " (e.g. git init,  git add . ,  git add foo.txt bar.html ,  \n" ;
	std::cout << " git commit,  git commit -m \"First commit\"  \n" ; 
    std::cout << " Type [q or Q] to quit\n\n" ;

    typedef std::string::const_iterator iterator_type;
    typedef teagit_grammar<iterator_type> teagit_grammar;

    teagit_grammar mygrammar; 

    std::string str;

    while (std::getline(std::cin, str))
    {
        if (str.empty() || str[0] == 'q' || str[0] == 'Q')
            break;

        std::string::const_iterator iter = str.begin();
        std::string::const_iterator end = str.end();
        bool r = phrase_parse(iter, end, mygrammar, space);

        if (r && iter == end)
        {
            std::cout << "-------------------------\n";
            std::cout << "Parsing succeeded\n";
            std::cout << "-------------------------\n";
        }
        else
        {
            std::string rest(iter, end);
            std::cout << "-------------------------\n";
            std::cout << "Parsing failed\n";
            std::cout << "stopped at: \": " << rest << "\"\n";
            std::cout << "-------------------------\n";
        }
    }

    std::cout << "Bye... :-) \n\n";
    return 0;
}


