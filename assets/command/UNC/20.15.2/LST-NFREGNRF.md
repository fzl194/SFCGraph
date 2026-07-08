---
id: UNC@20.15.2@MMLCommand@LST NFREGNRF
type: MMLCommand
name: LST NFREGNRF（查询本端NF和对端NRF实例的注册关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFREGNRF
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- NCG
- CBCF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF配置管理
- NF与NRF注册关系
status: active
---

# LST NFREGNRF（查询本端NF和对端NRF实例的注册关系）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、CBCF**

该命令用于查询本端NF和NRF实例的注册关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 本端NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元所部署的NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NRF（NRF）”：NRF类型<br>- “NON_NRF（non-NRF）”：非NRF类型<br>默认值：无<br>配置原则：<br>该参数需要与ADD NFPROFILE命令配置的本端NF类型一致。 |
| NRFINSTANCENAME | NRF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端NF所注册的对端NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：<br>该参数取自ADD NRF命令配置的NRF实例名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NFREGNRF]] · 本端NF和对端NRF实例的注册关系（NFREGNRF）

## 使用实例

假设要查询本端NF与对端NRF实例的注册关系，执行如下命令：

```
%%LST NFREGNRF:;%%
RETCODE = 0 操作成功

结果如下
------------------------
 本端NF类型 = NRF
NRF实例名称 = NRF_Instance_0
     优先级 = 10
       权重 = 100
（结果个数 = 1）

---- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFREGNRF.md`
