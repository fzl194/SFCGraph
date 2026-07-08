---
id: UDG@20.15.2@MMLCommand@LST UPUSRPROFCHG
type: MMLCommand
name: LST UPUSRPROFCHG（查询User Profile的计费配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPUSRPROFCHG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- UserProfile计费控制
status: active
---

# LST UPUSRPROFCHG（查询User Profile的计费配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询在线计费用户模板默认使能开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRPROFNAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USERPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPUSRPROFCHG]] · User Profile的计费配置（UPUSRPROFCHG）

## 使用实例

查询用户模板默认配额使能开关：

```
LST UPUSRPROFCHG: USRPROFNAME="userprofile1";
```

```

RETCODE = 0 操作成功

显示用户模板默认使能开关
------------------------
　　　　　　　　用户模板名称 = userprofile1
                   默认配额使能开关 = 开启
　　　新业务默认配额使能开关 = 继承
非新业务场景默认配额使能开关 = 关闭
(结果个数 = 1)
--END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPUSRPROFCHG.md`
