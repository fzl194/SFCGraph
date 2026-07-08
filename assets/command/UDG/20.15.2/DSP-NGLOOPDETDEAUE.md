---
id: UDG@20.15.2@MMLCommand@DSP NGLOOPDETDEAUE
type: MMLCommand
name: DSP NGLOOPDETDEAUE（显示5G LAN环路检测去活用户记录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NGLOOPDETDEAUE
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN环路检测配置
- 显示5G LAN环路检测去活用户记录
status: active
---

# DSP NGLOOPDETDEAUE（显示5G LAN环路检测去活用户记录）

## 功能

**适用NF：UPF**

该命令用于显示5G LAN环路检测去活用户记录信息。

## 注意事项

此命令包含个人数据，传出客户网络需要使用匿名化工具进行匿名化处理。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VnInstance以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGLOOPDETDEAUE]] · 5G LAN环路检测去活用户记录（NGLOOPDETDEAUE）

## 使用实例

查询当前5G LAN环路检测去活用户记录信息：

```
DSP NGLOOPDETDEAUE: VNINSTANCE="a0000001-460-01-01";
```

```

RETCODE = 0  操作成功

5G LAN环路检测去活用户记录
----------------------------------------------------------
Result  =  
 No   LoopType                        SessionReleaseId                ReservedSessionId                                 DeactiveTime                    DeactiveNum                     ReActiveTime                    AlarmStatus                     ConflictMac
                   
 0    N3-N3                           48456789012353                  48456789012342                                    22:57:11 03/18/2025(MM/DD/YYYY) 1                               NULL                            TRUE                            56-BB-CC-DD-EE-FF               

(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NGLOOPDETDEAUE.md`
