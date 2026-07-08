# 显示规则匹配控制信息下发状态（DSP RULEMATCHCTRL）

- [命令功能](#ZH-CN_CONCEPT_0000202791209836__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202791209836__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202791209836__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202791209836__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202791209836__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202791209836__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202791209836)

**适用NF：PGW-U、UPF**

该命令用来显示规则匹配时下发的控制信息状态。

#### [注意事项](#ZH-CN_CONCEPT_0000202791209836)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202791209836)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202791209836)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MATCHCTRLTYPE | 匹配控制类型 | 可选必选说明：必选参数<br>参数含义：规则匹配时选择的控制面信息类型。<br>数据来源：本端规划<br>取值范围：<br>- POLICY_INFO：表示选择匹配时使用的策略信息。<br>- SPECIFIED_USER：表示选择匹配时使用指定用户的规则。<br>默认值：无<br>配置原则：指定控制面信息类型。 |

#### [使用实例](#ZH-CN_CONCEPT_0000202791209836)

显示规则匹配时下发的控制信息状态：

```
DSP RULEMATCHCTRL: MATCHCTRLTYPE=POLICY_INFO;
```

```

RETCODE = 0  Operation succeeded

The Status Of Control Plane Information Installation Required For Rule Matching
-------------------------------------------------------------------------------
                                         Match Control Type  =  policy infomation
Rule Matching Control Plane Information Installation Status  =  done
                                       Rule matching result  =  The result is as follows							   
Userprofile1 = userprofile_test

(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202791209836)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 匹配控制类型 | 规则匹配时选择的控制面信息类型。 |
| 规则匹配控制信息安装状态 | 表示规则匹配控制信息的安装状态。 |
| 规则匹配结果 | 规则匹配结果。 |
