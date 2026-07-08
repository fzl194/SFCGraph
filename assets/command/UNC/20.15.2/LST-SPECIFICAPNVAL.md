---
id: UNC@20.15.2@MMLCommand@LST SPECIFICAPNVAL
type: MMLCommand
name: LST SPECIFICAPNVAL（查询用户APN与消息交互使用APN的映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SPECIFICAPNVAL
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 周边接口呈现APN策略管理
- 指定上报的APN
status: active
---

# LST SPECIFICAPNVAL（查询用户APN与消息交互使用APN的映射关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询用户APN与消息交互使用APN的映射关系。在配置用户APN与消息交互使用APN的映射关系过程中，运营商需要查询已有的映射关系时执行该命令。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERAPN | 用户APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户使用的别名APN、虚拟APN或真实APN名称。用户APN的优先级从高到低为：别名APN、虚拟APN、真实APN。软参DWORD1040 BIT28用于控制在AAA鉴权流程中是否使用ADD SPECIFICAPNVAL配置中的别名APN对用户使用的别名APN进行转换。软参DWORD1040 BIT29控制在AAA鉴权流程中，获取ADD SPECIFICAPNVAL配置所使用用户APN的优先级。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>必须是系统已经配置的APN或APN别名。 |

## 操作的配置对象

- [用户APN与消息交互使用APN的映射关系（SPECIFICAPNVAL）](configobject/UNC/20.15.2/SPECIFICAPNVAL.md)

## 使用实例

- 查询一个名为“huawei.com”的用户APN和与之对应的上报APN之间的映射关系：
  ```
  %%LST SPECIFICAPNVAL: SUBSCRIBERAPN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                    用户APN  =  huawei.com
   是否只对漫游用户生效开关  =  不使能
  PCRF交互消息使用的映射APN  =  pcrf
        CG话单使用的映射APN  =  NULL
   OCS交互消息使用的映射APN  =  NULL
   AAA计费消息使用的映射APN  =  NULL
   AAA鉴权消息使用的映射APN  =  NULL
   AAA鉴权消息使用的映射APN是否大小写敏感  =  大小写不敏感
   CHF交互消息使用的映射APN  =  NULL
   PCF交互消息使用的映射APN  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有用户APN与消息交互使用APN的映射关系：
  ```
  %%LST SPECIFICAPNVAL:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  用户APN     是否只对漫游用户生效开关  PCRF交互消息使用的映射APN  CG话单使用的映射APN  OCS交互消息使用的映射APN  AAA计费消息使用的映射APN  AAA鉴权消息使用的映射APN  AAA鉴权消息使用的映射APN是否大小写敏感  CHF交互消息使用的映射APN  PCF交互消息使用的映射APN  

  123         使能                      pcrf                       cg                   NULL                      NULL                      NULL                      大小写不敏感                            NULL                      NULL                      
  huawei.com  不使能                    pcrf                       NULL                 NULL                      NULL                      NULL                      大小写不敏感                            NULL                      NULL                      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户APN与消息交互使用APN的映射关系（LST-SPECIFICAPNVAL）_09653635.md`
