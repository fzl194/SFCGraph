---
id: UDG@20.15.2@MMLCommand@LST RELAYPROTODEF
type: MMLCommand
name: LST RELAYPROTODEF（查询媒体中继协议定义）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYPROTODEF
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继协议定义
status: active
---

# LST RELAYPROTODEF（查询媒体中继协议定义）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询媒体中继协议定义。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYPROTODEFNM | 媒体中继协议定义规则组名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体中继协议定义规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RELAYPROTORULE | 媒体中继协议定义规则 | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体中继协议定义规则。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYPROTODEF]] · 媒体中继协议定义（RELAYPROTODEF）

## 使用实例

假如需要查询一组媒体中继协议定义，则命令如下：

```
LST RELAYPROTODEF: RELAYPROTODEFNM="def001";
```

```

RETCODE = 0  操作成功
 
结果如下
------------------------
媒体中继协议定义规则组名称  =  def001
      媒体中继协议定义规则  =  rule001
                    优先级  =  1
          媒体中继协议类型  =  MP4
                  检测方式  =  通过查询参数
            路径参数关键字  =  NULL
            查询参数关键字  =  key1
                配置域名称  =  NULL
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYPROTODEF.md`
