---
id: UDG@20.15.2@MMLCommand@DSP RULEMATCHCTRL
type: MMLCommand
name: DSP RULEMATCHCTRL（显示规则匹配控制信息下发状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RULEMATCHCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则匹配测试
- 规则匹配控制面信息
status: active
---

# DSP RULEMATCHCTRL（显示规则匹配控制信息下发状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示规则匹配时下发的控制信息状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MATCHCTRLTYPE | 匹配控制类型 | 可选必选说明：必选参数<br>参数含义：规则匹配时选择的控制面信息类型。<br>数据来源：本端规划<br>取值范围：<br>- POLICY_INFO：表示选择匹配时使用的策略信息。<br>- SPECIFIED_USER：表示选择匹配时使用指定用户的规则。<br>默认值：无<br>配置原则：指定控制面信息类型。 |

## 操作的配置对象

- [安装规则匹配控制面信息（RULEMATCHCTRL）](configobject/UDG/20.15.2/RULEMATCHCTRL.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示规则匹配控制信息下发状态（DSP-RULEMATCHCTRL）_91209836.md`
