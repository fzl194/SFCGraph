---
id: UDG@20.15.2@MMLCommand@ADD PROTOCOLGROUP
type: MMLCommand
name: ADD PROTOCOLGROUP（增加自定义协议组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: PROTOCOLGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 延迟生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 协议组
status: active
---

# ADD PROTOCOLGROUP（增加自定义协议组）

## 功能

**适用NF：PGW-U、UPF**

该命令用来增加自定义协议组，输入值为PROTGROUPNAME，用来定义协议组名称。

## 注意事项

- 该命令执行后立即生效。
- 不允许PROTGROUPNAME为空的协议组名称。
- 整机支持100个协议组，包括默认的协议组数，其中默认协议组最大为20个，通过LOD SIGNATUREDB命令加载SA特征库时由系统内部产生，可配置的协议组最大为80。每个协议组下可配置1024种协议，协议组下配置的所有的协议个数不能超过3300个。
- 对于已绑定到FlowFilter的ProtocolGroup，在ProtocolGroup下配置新的Protocol最长会在60秒内生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：自定义协议组名不能与默认协议组重名。 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：可选参数<br>参数含义：协议组包含的协议的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令smctrldsp protocol-list查询。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTOCOLGROUP]] · 自定义协议组（PROTOCOLGROUP）

## 使用实例

如果想要添加一条名为“group1”的自定义协议组，应该输入合法的数据，例如：

```
ADD PROTOCOLGROUP:PROTGROUPNAME="group1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-PROTOCOLGROUP.md`
