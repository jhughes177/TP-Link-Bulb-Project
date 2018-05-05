BHC Ticketing App

An IOS ticketing for Boston Harbor Cruises

Prerequisites

Pods needed:

Stripe
AFNetworking
Alamofire

Documentation on how to install pods using CocoaPods here:

https://guides.cocoapods.org/using/using-cocoapods.html
https://guides.cocoapods.org/using/pod-install-vs-update.html

Built With
Swift - Programming language for Xcode App
AFNetworking - Networking Library
Stripe - SDK used for secure payment
Alamofire - Networking Library


Important Files:

Xcode:

FirtViewController.swift - Class for displaying data tableview
TicketViewControllet.swift - Class for displaying ticket view
CruiseTableConnection.swift - Class for connection to Cruise Table in database
Product.swift - Class that initializes cruise object variables
TicketCableConnection.swift - Class for connection to Ticket Sales Table in database
Ticket.swift - Class that initializes ticket object variables
APICommunication.swift - Class that communicates with Stripe
Main.storyboard - GUI Class

Server:

adminPortal.php -
loginPortal.php -
cofig.php -
connect.php -
connect2.php -
ticketGenerator.php -
web.php -

Authors
Jared Hughes

Acknowledgments/Documentations/Tutorials
Stripe Documentation - https://stripe.com/docs/mobile/ios/custom
MySQL Tutorial for Xcode Connection - https://www.simplifiedios.net/xcode-json-example-retrieve-data-mysql/
