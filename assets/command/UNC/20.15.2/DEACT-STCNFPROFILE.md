---
id: UNC@20.15.2@MMLCommand@DEACT STCNFPROFILE
type: MMLCommand
name: DEACT STCNFPROFILE（去激活手动注册的NFProfile）
nf: UNC
version: 20.15.2
verb: DEACT
object_keyword: STCNFPROFILE
command_category: 动作类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF信息导入管理
status: active
---

# DEACT STCNFPROFILE（去激活手动注册的NFProfile）

## 功能

**适用NF：NRF**

该命令用于去注册手动上线的NF。

该命令执行完成后，该NF将不能继续在网络中提供服务，但该NF的Profile文件还在NRF中，如果需要重新在网络中提供服务，直接执行手动注册命令即可。

## 注意事项

- 该命令执行后等待5s左右生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待手动去注册的NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [手动注册的NFProfile（STCNFPROFILE）](configobject/UNC/20.15.2/STCNFPROFILE.md)

## 使用实例

下线手动注册的NFProfile: 通过手动注册的实例标识为f717585b-cb76-484c-9302-6e9ce69d5623的NF，如果不需要再在网络中提供服务，可以通过执行如下命令去注册该NF。

```
DEACT STCNFPROFILE: NFINSTANCEID="f717585b-cb76-484c-9302-6e9ce69d5623";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/去激活手动注册的NFProfile（DEACT-STCNFPROFILE）_44006686.md`
