---
id: UDG@20.15.2@MMLCommand@LST GRAYUPTSTUSER
type: MMLCommand
name: LST GRAYUPTSTUSER（查询支持灰度升级拨测的用户）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GRAYUPTSTUSER
command_category: 查询类
applicable_nf:
- UPF
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 灰度升级拨测用户信息
status: active
---

# LST GRAYUPTSTUSER（查询支持灰度升级拨测的用户）

## 功能

**适用NF：UPF、SGW-U、PGW-U**

该命令用于查询拨测用户信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRAYUSERNAME | 拨测用户名称 | 可选必选说明：可选参数<br>参数含义：拨测用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GRAYUPTSTUSER]] · 灰度升级拨测用户（GRAYUPTSTUSER）

## 使用实例

查询拨测用户信息，命令为：

```
LST GRAYUPTSTUSER:;
```

```

RETCODE = 0  操作成功。

-----------------
                         拨测用户名称  =  test
                                 类型  =  IMSI
                                 IMSI  =  123243455465767
                      IMSI/MSISDN号段  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GRAYUPTSTUSER.md`
