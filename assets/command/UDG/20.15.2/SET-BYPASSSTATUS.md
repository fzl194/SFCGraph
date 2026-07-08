---
id: UDG@20.15.2@MMLCommand@SET BYPASSSTATUS
type: MMLCommand
name: SET BYPASSSTATUS（设置BYPASS状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: BYPASSSTATUS
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass状态管理
status: active
---

# SET BYPASSSTATUS（设置BYPASS状态）

## 功能

![](设置BYPASS状态（SET BYPASSSTATUS）_74020103.assets/notice_3.0-zh-cn.png)

设置进入BYPASS状态后，仅最小维护通道功能可用；设置退出BYPASS状态前请确认ALM-135644 节点存储亚健康告警已经恢复，请慎重使用该命令。

该功能仅支持华为虚拟化层软件FusionSphere，不支持第三方虚拟化层软件。

本命令用于手动设置部署的节点当前BYPASS状态。

若需要设置指定节点的BYPASS状态，需要输入“网元ID”和“节点名称”参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 该命令仅限系统管理员可以执行。
- 节点BYPASS状态的系统初始值为“Normal”，表示当前节点的Bypass状态为非Bypass状态。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| APPID | 网元ID | 可选必选说明：必选参数<br>参数含义：用于指示系统需要设置指定网元ID下的节点BYPASS状态。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：<br>“MEID”<br>获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。 |
| SETTYPE | 设置BYPASS状态类型 | 可选必选说明：必选参数<br>参数含义：用于指示系统需要设置的BYPASS状态。<br>取值范围：<br>- “enter(进入BYPASS)”<br>- “exit(退出BYPASS)”<br>默认值：无。<br>配置原则<br>- 本命令配置原则是根据当前存储对业务的影响来选择进入和退出BYPASS状态，存储状态可参考<br>“ALM-135644 节点存储亚健康”<br>。<br>- 在发生节点<br>“ALM-135644 节点存储亚健康”<br>时，用户可根据当前存储对业务的影响来选择是否需要进入BYPASS，如果需要手动进入BYPASS，则选择enter。<br>- 在节点“ALM-135644 节点存储亚健康”消失时，用户可根据当前存储对业务的影响来选择是否需要退出BYPASS，如果需要手动退出BYPASS，则选择exit。 |
| NODENAME | 节点名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要设置哪个节点的BYPASS状态。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示设置所有节点的BYPASS状态。<br>- 操作员在对应FusionStage页面“资源管理>节点管理>节点”查看相应的节点获得。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BYPASSSTATUS]] · BYPASS状态（BYPASSSTATUS）

## 使用实例

1. 设置“网元ID”为“0”的所有节点BYPASS状态：
    a. 操作成功。
      ```
      %%SET BYPASSSTATUS: APPID=0, SETTYPE=enter;%%
      RETCODE = 0  操作成功

      操作结果如下
      ------------
      网元ID  节点IP           节点名称         设置类型    

      0       10.0.0.1         10.0.0.1         进入BYPASS  
      0       10.0.0.2         10.0.0.2         进入BYPASS  
      0       10.0.0.3         10.0.0.3         进入BYPASS
      (结果个数 = 3)

      ---    END
      ```
    b. BYPASS模式未激活，操作失败。
      ```
      %%SET BYPASSSTATUS: APPID=0, SETTYPE=enter;%%
      RETCODE = 130002  操作失败

      操作结果如下
      ------------
      网元ID  节点IP           节点名称         设置类型         详细信息

      0       10.0.0.1         10.0.0.1         进入BYPASS       节点BYPASS模式未激活，命令无效  
      0       10.0.0.2         10.0.0.2         进入BYPASS       节点BYPASS模式未激活，命令无效
      0       10.0.0.3         10.0.0.3         进入BYPASS       节点BYPASS模式未激活，命令无效
      (结果个数 = 3) 

      ---    END
      ```
    c. BYPASS模式未激活，部分成功。
      ```
      %%SET BYPASSSTATUS: APPID=0, SETTYPE=enter;%%
      RETCODE = 130004  部分成功

      操作结果如下
      ------------
        网元ID  =  0
        节点IP  =  10.0.0.1
      节点名称  =  10.0.0.1
      设置类型  =  进入BYPASS
      详细信息  =  节点BYPASS模式未激活，命令无效。
      （结果个数 = 1）

      ---    END
      ```
2. 设置“网元ID”为“0”，“节点名称”为“10.0.0.1”的节点BYPASS状态：
    a. 操作成功。
      ```
      %%SET BYPASSSTATUS: APPID=0, SETTYPE=enter, NODENAME="10.0.0.1";%%
      RETCODE = 0  操作成功

      操作结果如下
      ------------
        网元ID  =  0
        节点IP  =  10.0.0.1
      节点名称  =  10.0.0.1
      设置类型  =  进入BYPASS
      (结果个数 = 1)

      ---    END
      ```
    b. BYPASS模式未激活。
      ```
      %%SET BYPASSSTATUS: APPID=0, SETTYPE=enter, NODENAME="10.0.0.1";%%
      RETCODE = 130002  操作失败

      操作结果如下
      ------------
        网元ID  =  0
        节点IP  =  10.0.0.1
      节点名称  =  10.0.0.1
      设置类型  =  进入BYPASS
      详细信息  =  节点BYPASS模式未激活，命令无效
      (结果个数 = 1) 

      ---    END
      ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-BYPASSSTATUS.md`
