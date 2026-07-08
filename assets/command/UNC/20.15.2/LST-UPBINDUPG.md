---
id: UNC@20.15.2@MMLCommand@LST UPBINDUPG
type: MMLCommand
name: LST UPBINDUPG（查询用户模板组和用户模板的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPBINDUPG
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板绑定
status: active
---

# LST UPBINDUPG（查询用户模板组和用户模板的绑定关系）

## 功能

**适用NF：PGW-C、SMF**

本命令用于查询UsrProfGroup下绑定的UserProfile。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的USERPROFGNAME必须是系统已经存在的UsrProfGroup对象名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPBINDUPG]] · 用户模板组和用户模板的绑定关系（UPBINDUPG）

## 使用实例

查询UserProfGName为userprofg1的UPBindUPG配置：

```
LST UPBINDUPG:USERPROFGNAME="userprofg1";
```

```

RETCODE = 0  操作成功。

用户模板组与用户模板绑定信息
----------------------------
     用户模板组名称  =  userprofg1
       用户模板名称  =  userprofile
                RAT  =  UTRAN
           漫游属性  =  本地
   计费属性配置模式  =  NULL
           计费属性  =  NULL
       计费属性掩码  =  0xFFFF
IMSI/MSISDN号段名称  =  NULL
     IMEISV号段名称  =  NULL
         位置组名称  =  NULL
             优先级  =  10
           缺省标记  =  0
         位置组名称  =  NULL
   用户模板绑定类型  =  SPECIFIC
 本地PCC策略选择模式 = 继承全局配置
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户模板组和用户模板的绑定关系（LST-UPBINDUPG）_09897232.md`
