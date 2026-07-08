---
id: UDG@20.15.2@MMLCommand@LST ERRORCODE
type: MMLCommand
name: LST ERRORCODE（查询错误码）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ERRORCODE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 重定向公共参数管理
- ErrorCode
status: active
---

# LST ERRORCODE（查询错误码）

## 功能

**适用NF：PGW-U、UPF**

此命令用于显示配置错误码信息。

## 注意事项

- 该命令执行后立即生效。
- 输入ERRORCODENAME查询指定记录，如果不输入ERRORCODENAME表示查询所有记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ERRORCODENAME | 错误码名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置错误码配置名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ERRORCODE]] · 错误码（ERRORCODE）

## 使用实例

查询所有错误码：

```
LST ERRORCODE:;
```

```

%%LST ERRORCODE:;%%
RETCODE = 0  Operation succeeded

Error Code
----------
Error Code Name  Error Code Range Operation  Error Code Start Value  Error Code End Value  

e1               Less Than or Equal To       0                       10                    
testerrorcode    Less Than or Equal To       0                       5                     
(Number of results = 2)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ERRORCODE.md`
