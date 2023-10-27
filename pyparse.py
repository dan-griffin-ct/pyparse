#!/usr/bin/env python3
import re
import argparse

# sample text
# note - working on building out parser to ingest text files
submitted_text = "Lorem! ipsum? dolor: sit; amet, consectetur. adipiscing elit. Sed rutrum fringilla nibh, sed pharetra felis maximus vel. Vivamus eu imperdiet elit. Curabitur congue vestibulum ligula, eu ultrices arcu suscipit a. Cras vel mi odio. Etiam pretium sodales elit id luctus. Maecenas ac aliquam lorem, vel imperdiet mi. Aliquam imperdiet lacinia leo a posuere. Cras vitae lectus at neque interdum venenatis id nec diam. Nunc non odio imperdiet dui dignissim luctus. Maecenas tempus augue sit amet libero suscipit lacinia. Aliquam blandit, leo id ultrices porta, enim est tincidunt arcu, vitae lobortis ante ipsum in libero. Nam imperdiet facilisis dui ac lacinia. Morbi quis mauris sed tortor hendrerit eleifend. Cras aliquam ante et sem pulvinar mattis. Curabitur vel magna lacinia, porttitor arcu a, aliquet arcu. Maecenas aliquet laoreet eros, eu consequat ipsum.\
Aliquam at enim porttitor, lobortis quam eget, suscipit dui. Morbi varius condimentum leo, eget tempus lectus vulputate ac. Cras vel neque tincidunt, pulvinar ipsum et, rutrum ex. Nunc tempus rutrum porta. Mauris nec pellentesque magna. Donec volutpat libero sit amet nulla euismod, tristique aliquam purus hendrerit. Maecenas sed diam in massa sagittis aliquam vitae ac orci.\
Donec odio nunc, mollis nec porttitor id, sodales ut ligula. Fusce ornare leo at suscipit ultrices. Pellentesque sit amet diam bibendum, bibendum elit nec, sagittis dolor. Suspendisse tempor, magna vitae interdum tristique, nulla libero gravida nulla, vel porttitor massa urna ac tellus. Praesent tortor ex, lobortis vel massa ac, ultrices consequat diam. Fusce tincidunt vehicula lorem, eget fermentum leo ultricies eget. Morbi condimentum, risus ut tincidunt fringilla, nulla urna ultricies eros, vel sagittis magna lectus vitae erat. Curabitur pulvinar vel ipsum vitae posuere. Aliquam et massa porttitor enim fermentum lacinia sed nec turpis.\
Nulla sagittis malesuada augue, et pellentesque arcu faucibus in. Curabitur consectetur urna sed sapien varius, eu imperdiet lectus commodo. Donec sagittis mi leo, ut aliquam dolor mollis in. Duis pellentesque tincidunt dolor. Morbi dapibus tempor euismod. Quisque nec nisl consectetur, interdum mauris sit amet, viverra lorem. Mauris congue diam turpis, nec ultrices leo iaculis et. Vivamus euismod sem nec sapien vestibulum lobortis eget vel libero. Mauris eleifend bibendum erat nec elementum. Mauris at mauris consectetur, aliquam diam id, pharetra elit. Aenean rutrum risus eget dolor condimentum, id volutpat eros tristique. Donec egestas et justo in posuere. Nullam mattis hendrerit mauris. Sed eu justo mi. Praesent blandit dui ut imperdiet dictum.\
Donec egestas efficitur est, quis porttitor diam scelerisque ut. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed pharetra tellus eu nisi lacinia mattis. Morbi congue volutpat quam, id vehicula nisi feugiat sed. Morbi posuere enim quis quam vulputate, ut ultricies urna imperdiet. Sed sit amet maximus erat. Mauris est tellus, finibus ut convallis in, imperdiet ut nunc. Nulla hendrerit justo diam, at ornare dui efficitur vulputate. Proin vestibulum purus elit, tempus semper mi viverra id. Aliquam diam tellus, placerat et tempor eget, malesuada non tortor. Donec hendrerit turpis vel elit ornare condimentum.\
Suspendisse sit amet neque et dolor accumsan consectetur. Sed sodales nec tortor vitae pulvinar. Quisque at velit id felis tincidunt ultricies sit amet tempor tortor. Integer dui velit, tincidunt non diam eget, scelerisque ornare ante. Curabitur sagittis orci gravida lectus sollicitudin, sollicitudin ultrices tortor ornare. Integer in eros orci. Vivamus felis erat, tempus a maximus eget, congue vitae dolor. Suspendisse dui odio, convallis quis lectus sit amet, ullamcorper fermentum est. Vestibulum quis tristique augue. Nulla a luctus nunc, et aliquet ipsum.\
Duis congue justo elit, vel pharetra justo khroncus non. Morbi velit sem, maximus ut libero in, viverra tempus metus. Proin gravida nunc ante, id sagittis dolor scelerisque eget. Phasellus sollicitudin lectus id mauris scelerisque, non sagittis eros congue. Praesent sodales faucibus dolor, eu gravida nunc mattis ac. Donec tincidunt ante ac dolor lacinia accumsan. Maecenas blandit pharetra mi, vitae hendrerit metus ornare quis.\
Donec sit amet dapibus neque. Proin semper mauris eget velit feugiat, eu finibus diam condimentum. Vestibulum ultrices odio velit, eu rutrum augue rhoncus interdum. Etiam quis nisl turpis. Sed et pharetra dui. Nunc a felis ut orci pellentesque tempor eget in odio. Etiam non urna molestie ante consequat efficitur convallis eget lorem. Duis laoreet eros vestibulum, porta lorem accumsan, accumsan ipsum. Sed a enim ac turpis vehicula dictum non quis tellus. In in ipsum lectus. Aenean nisl tortor, eleifend quis velit quis, tristique ultrices quam.\
Quisque at nisl id eros aliquet aliquet. Duis ut dictum leo, ac imperdiet dui. Aliquam id libero rhoncus, condimentum est at, ornare nibh. Proin efficitur imperdiet leo non tempus. Pellentesque auctor imperdiet dolor, vitae fringilla arcu consequat a. Nunc sed molestie odio. Donec vehicula mauris ut egestas bibendum. Fusce nisi ante, imperdiet vel iaculis nec, semper gravida nulla. Morbi dapibus metus eu feugiat pretium. Curabitur in eros tempor, consectetur eros vestibulum, pulvinar metus.\
Donec sed ipsum eget risus gravida consectetur sed at massa. Mauris porta feliz in elit rhoncus, sed tincidunt ligula convallis. Proin aliquet molestie eleifend. Vestibulum faucibus, elit eget condimentum volutpat, est velit facilisis justo, porta egestas velit sem at lectus. Nulla tempor eros elit, vel blandit erat pellentesque ut. Pellentesque mattis leo eu ante tristique ultrices non ac quam. Etiam luctus diam sed massa vulputate, sed molestie lorem pellentesque. Vivamus tincidunt quam eu nisi volutpat, vel molestie neque vehicula. Nam consequat enim nec mollis ultrices. Proin maximus nunc sit amet vestibulum porttitor. Donec nec volutpat odio. Sed sollicitudin magna id mollis euismod."

# allow user to decide if they want to include punctuation in end tally
parser = argparse.ArgumentParser("pyparse")
parser.add_argument("sanitize_punctuation", help="Passing True will exclude these characters from the count: ,.;:!?/\`")
args = parser.parse_args()

# convert str arg to boolean
remove_punctuation = True if args.sanitize_punctuation == "T" else False

print(f'remove_punctuation {remove_punctuation}')

# lower case
submitted_text_lower_case = submitted_text.lower()


# build alphabetized array out of words
presanitized_word_list = submitted_text_lower_case.split(" ")
print('presanitized_word_list', sorted(presanitized_word_list))


# word count 
word_count = len(presanitized_word_list)
print(f'word count: {word_count}')

if remove_punctuation:
    # remove white space and commonly used punctuation from word list
    sanitized_word_list = re.sub(r"[' ',.;:!?/\`]", "", submitted_text_lower_case)
else:
    print('false')
    # remove white space from word list
    sanitized_word_list = re.sub(r" ", "", submitted_text_lower_case)

print('char count:', len(sanitized_word_list))

# create dict to add tallies to
letter_dict = {}

# tally number of times each letter occurs in the submitted text
for letter in sanitized_word_list:
    if letter_dict.get(letter):
        # if found increment tally by one
        letter_dict[letter] += 1
    else:
        # else start tally
        letter_dict[letter] = 1

# sort letter tally dict
sorted_letter_dict = dict(sorted(letter_dict.items()))

print(f'sorted letter dict: \n {sorted_letter_dict}')
