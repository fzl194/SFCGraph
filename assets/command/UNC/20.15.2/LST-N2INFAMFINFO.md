---
id: UNC@20.15.2@MMLCommand@LST N2INFAMFINFO
type: MMLCommand
name: LST N2INFAMFINFO（查询AMF的N2接口信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N2INFAMFINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF的N2接口信息管理
status: active
---

# LST N2INFAMFINFO（查询AMF的N2接口信息）

## 功能

**适用NF：AMF**

该命令用于查询当前AMF的N2接口信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N2INFAMFINFO]] · AMF的N2接口信息（N2INFAMFINFO）

## 使用实例

运营商A需要查询当前AMF的N2接口信息。

```
%%LST N2INFAMFINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
     NF实例名称  =  AMF_Instance_0
     IP地址类型  =  IPTypeV4
  IPV4类型地址1  =  192.168.0.1
  IPV4类型地址2  =  192.168.0.2
  IPV4类型地址3  =  0.0.0.0
  IPV4类型地址4  =  0.0.0.0
  IPV6类型地址1  =  ::
  IPV6类型地址2  =  ::
  IPV6类型地址3  =  ::
  IPV6类型地址4  =  ::
        AMF名称  =  amf1.cluster1.net2.3gppnetwork.org
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF的N2接口信息（LST-N2INFAMFINFO）_09652704.md`
