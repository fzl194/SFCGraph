---
id: UNC@20.15.2@MMLCommand@DSP UPDYNAMICINFO
type: MMLCommand
name: DSP UPDYNAMICINFO（显示UP节点动态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UPDYNAMICINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP动态信息
status: active
---

# DSP UPDYNAMICINFO（显示UP节点动态信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示UP节点动态信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示查询UP动态信息或根据UPF实例名称查询指定UPF的动态信息。<br>数据来源：本端规划<br>取值范围：<br>- ALL（所有）<br>- NFINSTANCENAME（UPF实例名称）<br>默认值：无<br>配置原则：无 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：该参数在"QUERYTYPE"配置为"NFINSTANCENAME"时为条件必选参数。<br>参数含义：该参数用于表示UPF的实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPDYNAMICINFO]] · UP节点动态信息（UPDYNAMICINFO）

## 使用实例

- 查询实例名为upf1的UPF的动态信息，需要执行以下命令：
  ```
  %%DSP UPDYNAMICINFO: QUERYTYPE=NFINSTANCENAME, NFINSTANCENAME="upf1";%%
  RETCODE = 0  操作成功

  结果如下
  ----------------
            UPF实例名称  =  upf1
                  LCI值  =  0
                  OCI值  =  0
            OCI解除时间  =  1970-01-01 00:00:00
            故障APN列表  =  []
            故障RAN列表  =  []
           智能单元状态  =  正常
       质差智能业务状态  =  正常
       体验智能业务状态  =  正常
  (结果个数 = 1)

  ---    END
  ```
- 查询所有UPF的动态信息，需要执行以下命令：
  ```
  %%DSP UPDYNAMICINFO: QUERYTYPE=ALL;%%
  RETCODE = 0  操作成功

  结果如下
  ----------------
  UPF实例名称     LCI值    OCI值    OCI解除时间           故障APN列表       故障RAN列表    智能单元状态    质差智能业务状态    体验智能业务状态
  upf1            0        0        1970-01-01 00:00:00   []                []             正常            正常                正常
  upf2            0        0        1970-01-01 00:00:00   []                []             正常            正常                正常                           
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-UPDYNAMICINFO.md`
