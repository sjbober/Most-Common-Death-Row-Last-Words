from bs4 import BeautifulSoup

#this file generates a list called listwords (without duplicates) that is a combination of stop words and top 100 words as defined by wikipedia

#got this list of stop words from https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
stopwords = ('ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than')

#these are other words that show up in the statements that don't seem important
other_words = ["sir","warden","ask","yes","thing","things","let","going","tell"]
wiki = '''
<table class="wikitable">


<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>1</td>
<td>the
</td></tr>
<tr>
<td>2</td>
<td>be
</td></tr>
<tr>
<td>3</td>
<td>to
</td></tr>
<tr>
<td>4</td>
<td>of
</td></tr>
<tr>
<td>5</td>
<td>and
</td></tr>
<tr>
<td>6</td>
<td>a
</td></tr>
<tr>
<td>7</td>
<td>in
</td></tr>
<tr>
<td>8</td>
<td>that
</td></tr>
<tr>
<td>9</td>
<td>have
</td></tr>
<tr>
<td>10</td>
<td>I
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>11</td>
<td>it
</td></tr>
<tr>
<td>12</td>
<td>for
</td></tr>
<tr>
<td>13</td>
<td>not
</td></tr>
<tr>
<td>14</td>
<td>on
</td></tr>
<tr>
<td>15</td>
<td>with
</td></tr>
<tr>
<td>16</td>
<td>he
</td></tr>
<tr>
<td>17</td>
<td>as
</td></tr>
<tr>
<td>18</td>
<td>you
</td></tr>
<tr>
<td>19</td>
<td>do
</td></tr>
<tr>
<td>20</td>
<td>at
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>21</td>
<td>this
</td></tr>
<tr>
<td>22</td>
<td>but
</td></tr>
<tr>
<td>23</td>
<td>his
</td></tr>
<tr>
<td>24</td>
<td>by
</td></tr>
<tr>
<td>25</td>
<td>from
</td></tr>
<tr>
<td>26</td>
<td>they
</td></tr>
<tr>
<td>27</td>
<td>we
</td></tr>
<tr>
<td>28</td>
<td>say
</td></tr>
<tr>
<td>29</td>
<td>her
</td></tr>
<tr>
<td>30</td>
<td>she
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>31</td>
<td>or
</td></tr>
<tr>
<td>32</td>
<td>will
</td></tr>
<tr>
<td>33</td>
<td>an
</td></tr>
<tr>
<td>34</td>
<td>my
</td></tr>
<tr>
<td>35</td>
<td>one
</td></tr>
<tr>
<td>36</td>
<td>all
</td></tr>
<tr>
<td>37</td>
<td>would
</td></tr>
<tr>
<td>38</td>
<td>there
</td></tr>
<tr>
<td>39</td>
<td>their
</td></tr>
<tr>
<td>40</td>
<td>what
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>41</td>
<td>so
</td></tr>
<tr>
<td>42</td>
<td>up
</td></tr>
<tr>
<td>43</td>
<td>out
</td></tr>
<tr>
<td>44</td>
<td>if
</td></tr>
<tr>
<td>45</td>
<td>about
</td></tr>
<tr>
<td>46</td>
<td>who
</td></tr>
<tr>
<td>47</td>
<td>get
</td></tr>
<tr>
<td>48</td>
<td>which
</td></tr>
<tr>
<td>49</td>
<td>go
</td></tr>
<tr>
<td>50</td>
<td>when
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>51</td>
<td>me
</td></tr>
<tr>
<td>52</td>
<td>make
</td></tr>
<tr>
<td>53</td>
<td>can
</td></tr>
<tr>
<td>54</td>
<td>like
</td></tr>
<tr>
<td>55</td>
<td>time
</td></tr>
<tr>
<td>56</td>
<td>no
</td></tr>
<tr>
<td>57</td>
<td>just
</td></tr>
<tr>
<td>58</td>
<td>him
</td></tr>
<tr>
<td>59</td>
<td>know
</td></tr>
<tr>
<td>60</td>
<td>take
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>61</td>
<td>person
</td></tr>
<tr>
<td>62</td>
<td>into
</td></tr>
<tr>
<td>63</td>
<td>year
</td></tr>
<tr>
<td>64</td>
<td>your
</td></tr>
<tr>
<td>65</td>
<td>good
</td></tr>
<tr>
<td>66</td>
<td>some
</td></tr>
<tr>
<td>67</td>
<td>could
</td></tr>
<tr>
<td>68</td>
<td>them
</td></tr>
<tr>
<td>69</td>
<td>see
</td></tr>
<tr>
<td>70</td>
<td>other
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>71</td>
<td>than
</td></tr>
<tr>
<td>72</td>
<td>then
</td></tr>
<tr>
<td>73</td>
<td>now
</td></tr>
<tr>
<td>74</td>
<td>look
</td></tr>
<tr>
<td>75</td>
<td>only
</td></tr>
<tr>
<td>76</td>
<td>come
</td></tr>
<tr>
<td>77</td>
<td>its
</td></tr>
<tr>
<td>78</td>
<td>over
</td></tr>
<tr>
<td>79</td>
<td>think
</td></tr>
<tr>
<td>80</td>
<td>also
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>81</td>
<td>back
</td></tr>
<tr>
<td>82</td>
<td>after
</td></tr>
<tr>
<td>83</td>
<td>use
</td></tr>
<tr>
<td>84</td>
<td>two
</td></tr>
<tr>
<td>85</td>
<td>how
</td></tr>
<tr>
<td>86</td>
<td>our
</td></tr>
<tr>
<td>87</td>
<td>work
</td></tr>
<tr>
<td>88</td>
<td>first
</td></tr>
<tr>
<td>89</td>
<td>well
</td></tr>
<tr>
<td>90</td>
<td>way
</td></tr></tbody></table>
</div>
<div style="float: left">
<table class="wikitable">

<tbody><tr>
<th style="width:3em;">Rank
</th>
<th style="width:4em;">Word
</th></tr>
<tr>
<td>91</td>
<td>even
</td></tr>
<tr>
<td>92</td>
<td>new
</td></tr>
<tr>
<td>93</td>
<td>want
</td></tr>
<tr>
<td>94</td>
<td>because
</td></tr>
<tr>
<td>95</td>
<td>any
</td></tr>
<tr>
<td>96</td>
<td>these
</td></tr>
<tr>
<td>97</td>
<td>give
</td></tr>
<tr>
<td>98</td>
<td>day
</td></tr>
<tr>
<td>99</td>
<td>most
</td></tr>
<tr>
<td>100</td>
<td>us
</td></tr></tbody></table>
'''
#top 100 words
soup = BeautifulSoup(wiki, "html.parser") #parse the wiki list of top 100 words
tags = soup('td')

#create a list and append all the top 100 wiki words to it
listwords = list()
for i in range(len(tags)):
	if i % 2 == 0:
		continue
	else:
		listwords.append(tags[i].text.strip())

for i in range(len(stopwords)): #adds stop words to the common words list if it's not in there already
    if stopwords[i] in listwords:
        continue
    else:
        listwords.append(stopwords[i])

for i in other_words:
	if i in listwords:
		continue
	else:
		listwords.append(i)
