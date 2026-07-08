---
id: UDG@20.15.2@MMLCommand@LST SPECIFICAPNVAL
type: MMLCommand
name: LST SPECIFICAPNVAL（查询用户APN与消息交互使用APN的映射关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SPECIFICAPNVAL
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- 指定上报的APN
status: active
---

# LST SPECIFICAPNVAL（查询用户APN与消息交互使用APN的映射关系）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询用户APN与消息交互使用APN的映射关系。在配置用户APN与消息交互使用APN的映射关系过程中，运营商需要查询已有的映射关系时执行该命令。

## 注意事项

- 要查询的映射关系记录必须是已经添加配置过的。
- 可以查询单条映射或全部已有的映射关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBERAPN | 用户APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户使用的别名APN、虚拟APN或真实APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：当查询单条映射关系时，必须输入已经配置过映射关系的APN名称。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SPECIFICAPNVAL]] · 用户APN与消息交互使用APN的映射关系（SPECIFICAPNVAL）

## 使用实例

- 查询一个名为“apn1.com”的用户APN和与之对应的上报APN之间的映射关系：
  ```
  LST SPECIFICAPNVAL:SUBSCRIBERAPN="apn1.com";
  ```
  ```

  RETCODE = 0  操作成功。

  用户APN映射信息
  ---------------
                  用户APN  =  apn1.com
      头增强使用的映射APN  =  NULL
               配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有用户APN与消息交互使用APN的映射关系：
  ```
  LST SPECIFICAPNVAL:;
  ```
  ```

  RETCODE = 0  操作成功。

  用户APN映射信息
  ---------------
  用户APN    头增强使用的映射APN    配置域名称

  apn1.com   NULL                   NULL          
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SPECIFICAPNVAL.md`
