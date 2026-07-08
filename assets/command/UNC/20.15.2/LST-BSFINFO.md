---
id: UNC@20.15.2@MMLCommand@LST BSFINFO
type: MMLCommand
name: LST BSFINFO（查询BSF信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BSFINFO
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# LST BSFINFO（查询BSF信息）

## 功能

**适用NF：SMF**

该命令用于查询BSF实例信息。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINSTANCENAME | BSF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BSF的实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。<br>默认值：无<br>配置原则：<br>该参数需要在ADD NFUUID中事先配置，可执行LST NFUUID进行查看。 |

## 操作的配置对象

- [BSF信息（BSFINFO）](configobject/UNC/20.15.2/BSFINFO.md)

## 使用实例

查询BSF实例信息：

```
%%LST BSFINFO:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  BSF实例名称 =  BSF_Instance_0
      BSF名称 =  bsf1.cluster1.net1.bsf.5gc
PLMN间BSF名称 = NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BSF信息（LST-BSFINFO）_09653008.md`
