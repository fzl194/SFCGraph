---
id: UNC@20.15.2@MMLCommand@DSP BYPASSSTATUS
type: MMLCommand
name: DSP BYPASSSTATUS（查询BYPASS状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BYPASSSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass状态管理
status: active
---

# DSP BYPASSSTATUS（查询BYPASS状态）

## 功能

![](查询BYPASS状态（DSP BYPASSSTATUS）_74020102.assets/notice_3.0-zh-cn_2.png)

该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。

本命令用于查询节点当前的BYPASS状态。

若需要查询指定节点的BYPASS状态，需要输入“网元ID”和“节点名称”参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| APPID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要查询指定网元ID下的节点BYPASS状态。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：<br>“网元ID”<br>获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。 |
| NODENAME | 节点名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要查询哪个节点的BYPASS状态。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示查询所有节点的信息。<br>- 用户可以通过[**DSP NODE**](../节点管理/节点查询（DSP NODE）_71678755.md)命令查看相应的节点名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BYPASSSTATUS]] · BYPASS状态（BYPASSSTATUS）

## 使用实例

1. 查询“网元ID”为“0”的所有节点BYPASS状态：
  ```
  %%DSP BYPASSSTATUS: APPID=0;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  网元ID  节点IP           节点名称         查询状态      手工进入BYPASS      节点BYPASS状态      详细信息
  0       10.0.0.1         10.0.0.1         Success       No                  Normal              Success             
  0       10.0.0.2         10.0.0.2         Success       No                  Normal              Success  
  0       10.0.0.3         10.0.0.3         Success       No                  Normal              Success             
  (结果个数 = 3)

  ---    END
  ```
2. 查询“网元ID”为“0”，“节点名称”为“10.0.0.1”的节点BYPASS状态：
  ```
  %%DSP BYPASSSTATUS: APPID=0, NODENAME="10.0.0.1";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
              网元ID  =  0
              节点IP  =  10.0.0.1
            节点名称  =  10.0.0.1
            查询状态  =  Success
      手工进入BYPASS  =  Yes
      节点BYPASS状态  =  Bypass
            详细信息  =  Success
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BYPASSSTATUS.md`
