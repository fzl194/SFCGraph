---
id: UNC@20.15.2@MMLCommand@LST NRFIMSDNN
type: MMLCommand
name: LST NRFIMSDNN（查询IMS PCF的DNN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFIMSDNN
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- IMS PCF的DNN信息管理
status: active
---

# LST NRFIMSDNN（查询IMS PCF的DNN）

## 功能

**适用NF：NRF**

该命令用于在NRF上查询配置的DNN信息。

若查询配置的全部DNN信息，请不要输入参数。

若查询配置的某个DNN信息，请输入“DNN”。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IMS PCF的数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。字符串类型，输入长度范围是0~64。该参数不区分大小写。<br>默认值：无<br>配置原则：<br>PCF支持的DNN等于或包含了配置的DNN信息，即认为该DNN在配置中已生效。<br>NRF上认为PCF是独立部署的条件是，PCF携带的DNN信息全部在NRF上已配置。<br>例如：<br>PCF规划支持ims.xa和ims.gz两个DNN：<br>当只配置一条“ims”记录时，NRF认为其是独立部署的；<br>当配置两条“ims.xa”和“ims.gz”记录时，NRF认为其是独立部署的；<br>当只配置一条“ims.xa”记录时，NRF认为其是非独立部署的。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFIMSDNN]] · IMS PCF的DNN（NRFIMSDNN）

## 使用实例

查询NRF上配置的全部DNN信息：

```
LST NRFIMSDNN:;
%%LST NRFIMSDNN:;%%
RETCODE = 0  操作成功

结果如下
------------------------
数据网络名称        

huawei.com  
ims         
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMS-PCF的DNN（LST-NRFIMSDNN）_96242306.md`
