---
id: UNC@20.15.2@MMLCommand@RMV NRFDNNDNAIRT
type: MMLCommand
name: RMV NRFDNNDNAIRT（删除DNN中数据网络访问标识最长后缀匹配转发路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFDNNDNAIRT
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
- DNN路由管理
status: active
---

# RMV NRFDNNDNAIRT（删除DNN中数据网络访问标识最长后缀匹配转发路由）

## 功能

**适用NF：NRF**

该命令用于删除DNN中数据网络访问标识最长后缀匹配转发路由。该命令功能暂不生效。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>取值为*时表示通配DNN。 |
| DNAISUFFIX | 数据网络访问标识后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络访问标识后缀。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于DNN寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示通过DNN中数据网络访问标识最长后缀匹配转发路由寻址的NF类型。该参数功能暂不生效。<br>数据来源：本端规划<br>取值范围：<br>- SMF（SMF）<br>- UPF（UPF）<br>默认值：无<br>配置原则：<br>当前只支持NF类型为SMF的路由。 |

## 操作的配置对象

- [DNN中数据网络访问标识最长后缀匹配转发路由（NRFDNNDNAIRT）](configobject/UNC/20.15.2/NRFDNNDNAIRT.md)

## 使用实例

运营商需要删除基于DNN为ims，数据网络访问标识后缀为huawei.com，选择SMF指向L-NRF1的路由时，执行此命令：

```
RMV NRFDNNDNAIRT: DNN="ims", DNAISUFFIX="huawei.com", NEXTNRFGRPNAME="L-NRF1", NFTYPE=SMF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNN中数据网络访问标识最长后缀匹配转发路由（RMV-NRFDNNDNAIRT）_92900874.md`
