---
id: UDG@20.15.2@MMLCommand@DSP POOLUSAGE
type: MMLCommand
name: DSP POOLUSAGE（显示地址池使用情况）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: POOLUSAGE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池使用情况
status: active
---

# DSP POOLUSAGE（显示地址池使用情况）

## 功能

**适用NF：PGW-U、UPF**

此命令用于显示地址池的信息。

## 注意事项

- 查询结果相对地址实际释放的时间有1-5秒的延迟。
- 地池使用率仅限本地地址池生效，外部地址池不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：必选参数<br>参数含义：地址池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOL命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@POOLUSAGE]] · 地址池使用情况（POOLUSAGE）

## 使用实例

查询地址池名称为testpool的地址池使用率信息：

```
DSP POOLUSAGE:POOLNAME="testpool";
```

```

RETCODE = 0  操作成功

地址池使用情况
-------------------------
                    Pool Usage (%)  =  0
            Total IP Address Count  =  0
          Invalid IP Address Count  =  0
                         Pool Name  =  testpool
  Wait-to-Release IP Address Count  =  0
             Used IP Address Count  =  0
                     Section Count  =  0
                   Locked IP Count  =  0
Used and Conflict Ip Address Count  =  0
  Used and Locked Ip Address Count  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-POOLUSAGE.md`
