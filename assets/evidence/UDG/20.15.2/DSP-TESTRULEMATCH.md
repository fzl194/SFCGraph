# 查询规则匹配测试结果（DSP TESTRULEMATCH）

- [命令功能](#ZH-CN_CONCEPT_0000202990168657__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202990168657__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202990168657__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202990168657__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202990168657__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202990168657__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202990168657)

**适用NF：PGW-U、UPF**

该命令用来获取匹配结果。

#### [注意事项](#ZH-CN_CONCEPT_0000202990168657)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202990168657)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202990168657)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000202990168657)

显示规则匹配结果：

```
DSP TESTRULEMATCH:;
```

```

RETCODE = 0  Operation succeeded

Rule Match Result Information
-----------------------------
Match Result  =  
                      PCC Policy:
                       Rule Name = rule01
                     Filter Name = filter1l34
                Flow Filter Name = flowfilter1
               PccPolicyGrp Name = pccgp1
                   upUrr(ONLINE) = cbbid-34000
                 upUrrID(ONLINE) = 234000
                   dnUrr(ONLINE) = cbbid-34000
                 dnUrrID(ONLINE) = 234000
                  upUrr(OFFLINE) = cbbid-34000off
                upUrrID(OFFLINE) = 134000
                  dnUrr(OFFLINE) = cbbid-34000off
                dnUrrID(OFFLINE) = 134000

(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202990168657)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 匹配结果 | 用于存放匹配结果。 |
