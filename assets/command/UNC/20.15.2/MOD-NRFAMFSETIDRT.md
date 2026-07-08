---
id: UNC@20.15.2@MMLCommand@MOD NRFAMFSETIDRT
type: MMLCommand
name: MOD NRFAMFSETIDRT（修改AMF集合标识路由）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFAMFSETIDRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- AMF集合标识路由管理
status: active
---

# MOD NRFAMFSETIDRT（修改AMF集合标识路由）

## 功能

**适用NF：NRF**

该命令用于修改指定AMF集合标识路由所归属的NRF实例组名称。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFSETID | AMF集合标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示AMF集合标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。按照十六进制输入，输入时不带0x，不足三位时从左边补0，取值范围0~3ff。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于AMF集合标识寻址AMF时的下一跳NRF实例组名称，被寻址的AMF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFAMFSETIDRT]] · AMF集合标识路由（NRFAMFSETIDRT）

## 使用实例

运营商网络规划变更，当前NRF上寻址AMF集合标识下一跳路由发生变化，AMF集合标识为086 的AMF所归属NRF实例组名称由“L-NRF1”变为“L-NRF3”，需要在当前NRF上执行：

```
MOD NRFAMFSETIDRT:AMFSETID="086",NEXTNRFGRPNAME="L-NRF3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改AMF集合标识路由（MOD-NRFAMFSETIDRT）_09653674.md`
