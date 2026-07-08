---
id: UNC@20.15.2@MMLCommand@LST BSFIPRANGEBIND
type: MMLCommand
name: LST BSFIPRANGEBIND（查询BSF实例与IPRANGE之间的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BSFIPRANGEBIND
command_category: 查询类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# LST BSFIPRANGEBIND（查询BSF实例与IPRANGE之间的绑定关系）

## 功能

**适用NF：SMF**

该命令用于查询BSF（Binding Support Function）所管辖的IP地址范围。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINSTANCENAME | BSF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BSF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>该参数需要在ADD NFUUID中事先配置，可执行LST NFUUID进行查看。 |
| IPRANGENAME | IPRANGE名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该BSF实例所管辖的IP地址范围的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSFIPRANGEBIND]] · BSF实例与IPRANGE之间的绑定关系（BSFIPRANGEBIND）

## 使用实例

查询所有的BSF实例所管辖的IP地址范围：

```
%%LST BSFIPRANGEBIND:;%%
RETCODE = 0  操作成功

结果如下
--------
         BSF实例名称  =  BSF_Instance_0
         IPRANGE名称  =  range1
         IPRANGE类型  =  IPv4地址类型
IPv4地址段范围起始值  =  192.168.2.1
IPv4地址段范围结束值  =  192.168.2.10
  IPv4地址段归属的域  =  NULL
IPv6前缀段范围起始值  =  ::
IPv6前缀段范围结束值  =  ::
             APN名称  =  NULL
       绑定的APN组名  =  NULL
  绑定的IPDOMAIN组名  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BSFIPRANGEBIND.md`
