---
id: UNC@20.15.2@MMLCommand@RMV ALLOWEDNSSAIS
type: MMLCommand
name: RMV ALLOWEDNSSAIS（删除允许访问的切片）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ALLOWEDNSSAIS
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 授权管理
- 访问授权控制
- 网络切片访问授权控制
status: active
---

# RMV ALLOWEDNSSAIS（删除允许访问的切片）

## 功能

**适用NF：NRF**

该命令用于删除指定NF对象所允许访问的切片信息。

当某个NF不再通过NRF限制特定切片的NF访问，可以通过此命令删除允许访问的NF切片信息。

## 注意事项

- 该命令执行后并不会立即生效，需要执行CMT ALLOWPLCY命令后生效。

- 当所有允许访问属性被删除后，表示针对此对象在NRF上的设置是可以被任何切片的NF实例访问。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OBJNAME | 授权对象名称 | 可选必选说明：必选参数<br>参数含义：该参数表示设置访问授权控制的NF对象名称，该参数可通过LST ALLOWEDOBJNAME命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| ALLOWEDSST | 允许访问该对象的SST | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定NF对象所允许访问的SST。SST表示切片业务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| ALLOWEDSD | 允许访问该对象的SD | 可选必选说明：必选参数<br>参数含义：该参数用于表示指定NF对象所允许访问的SD。SD表示切片差异描述，即针对上述相同SST再根据用户群等进一步细分的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [允许访问的切片（ALLOWEDNSSAIS）](configobject/UNC/20.15.2/ALLOWEDNSSAIS.md)

## 使用实例

授权对象objname001可以被多个切片访问，其中包含SST为2的切片。运营商根据需要，不允许SST为2,SD为010101的切片信息的NF继续访问objname001时，执行下面命令：

```
RMV ALLOWEDNSSAIS:OBJNAME="objname001",ALLOWEDSST=2,ALLOWEDSD="010101";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除允许访问的切片（RMV-ALLOWEDNSSAIS）_09651820.md`
