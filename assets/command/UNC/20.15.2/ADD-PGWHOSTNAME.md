---
id: UNC@20.15.2@MMLCommand@ADD PGWHOSTNAME
type: MMLCommand
name: ADD PGWHOSTNAME（增加逻辑接口的PGW主机名）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PGWHOSTNAME
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- P-GW Host Name配置
- P-GW逻辑接口主机名
status: active
---

# ADD PGWHOSTNAME（增加逻辑接口的PGW主机名）

## 功能

**适用NF：PGW-C**

此命令用于添加PGW-C逻辑接口主机名。该配置体现在PGW-C发送给Diameter AAA的授权请求消息AAR的PDN GW Identity中。用户从non-3GPP网络切换到3GPP网络时，MME需要根据hostname选择PGW-C，因此PGW-C上hostname的配置需要与DNS上的相关配置保持一致。

根据网络规划，当需要修改逻辑接口主机名时，需要先执行RMV PGWHOSTNAME命令，再执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 一个逻辑接口最多只能配置一个主机名。

- 最多可输入2条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：本端规划<br>取值范围：<br>- S5_P_OR_GN_OR_S2B（S5-P/Gn/S2b/S2a接口）<br>- S8_P_OR_GP_OR_S2B（S8-P/Gp/S2b/S2a接口）<br>默认值：无<br>配置原则：无 |
| PGWHOSTNAME | PGW-C主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名，需整网规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不支持空格，必须是可见ASCII码，不区分大小写。<br>默认值：无<br>配置原则：<br>- 依照协议，主机名的配置包含三个标签，格式如：<"topon" \| "topoff">.<single-label-interface-name>.<canonical-node-name>。例如：topon.S2b.gw4.cluster1.net27.operator.com。<br>- "topon" \| "topoff"：指示该主机名是否配置了拓扑信息。开启智能网关选择特性时建议配置为topon，否则只能进行合一节点的选择。<br>- single-label-interface-name：接口名称，仅作为一个标识，并非实际的物理接口。<br>- canonical-node-name：规范的节点名称，可以体现不同主机名间的拓扑关系。从末尾的点分名称开始比较，相同的点分名称越多，表明两个主机名称之间的拓扑关系越近。<br>- 即使其他两个标签完全相同，接口名称不同，也代表不同的主机名，即主机名称不等同于网元节点名称。 |

## 操作的配置对象

- [逻辑接口的PGW主机名（PGWHOSTNAME）](configobject/UNC/20.15.2/PGWHOSTNAME.md)

## 使用实例

根据网络规划，需要新增一个PGW主机名称为“topon.Eth-0.canonical-node-name.gw32.california.west.example.com”，和逻辑接口S5_P_OR_GN_OR_S2B绑定：

```
ADD PGWHOSTNAME:PGWHOSTNAME="topon.Eth-0.canonical-node-name.gw32.california.west.example.com",INTFTYPE=S5_P_OR_GN_OR_S2B;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加逻辑接口的PGW主机名（ADD-PGWHOSTNAME）_64343865.md`
