---
id: UNC@20.15.2@MMLCommand@REB NODE
type: MMLCommand
name: REB NODE（节点重建）
nf: UNC
version: 20.15.2
verb: REB
object_keyword: NODE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# REB NODE（节点重建）

## 功能

![](节点重建（REB NODE）_71765323.assets/notice_3.0-zh-cn_2.png)

重装节点，系统存储将会改变，业务将会中断，并可能会引起数据盘重新挂载，请慎重使用该命令。

本命令用于重装指定网元ID下指定名称的节点，重建方式分为重装OS和重建VM。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。
>
> - 当重建虚拟机操作完成之后，会在15~20分钟后恢复虚拟机密码为重建前密码。
> - 当节点开启双因子认证时，重建节点会导致双因子认证能力丢失，需要重新开启。

## 注意事项

- 对于不支持重建节点的第三方虚拟化层，无法使用该功能。
- 执行该命令会影响所有运行在该节点上的业务，以及节点的系统盘和数据盘，请慎重使用该命令。
- 重装OS会更换VM的系统盘；重建VM过程中会影响业务的正常运行，操作完成后业务无影响。
- 补丁场景进行节点重建后OS内核补丁需要等待15分钟后重启虚拟机生效。
- 重建VM可能会导致数据丢失，请谨慎使用。
- 重建OMU节点注意事项：
  当一个OMU节点重建后，会从另外一个OMU节点同步数据，请按照如下步骤确认OMU之间数据同步完成后才能进行其它节点的操作（重启/重建/重装）。
  禁止在一个OMU节点重建过程中或者OMU之间数据未同步完成场景操作（重启/重建/重装）另外一个OMU或者其它业务节点。
  确认OMU节点间的数据是否同步完成步骤如下：

  1. 确认ACS数据同步完成。
      执行 **DSP OMU** 命令， “SERVICEINSTANCE” 选择 “ACS” ，查询结果中 “倒换状态” ，为 “就绪” ，即表示ACS数据同步已完成。
    2. 确认GaussDB数据同步完成。
          a. 选择“ 应用配置 > 服务治理 ”界面，选择UNC，然后搜索GaussDB服务，查看属性列中status字段。确认两个实例内容分别为 “S”，“M”。
          b. 选择“ 监控分析 > 告警管理 > 活动告警 ”界面，确认无"ALM-126000 GaussDB组件故障"告警。
          c. 选择“ 监控分析 > 性能监控 > 业务监控 > GaussDB服务实例 > GaussDB服务数据库监控 ”界面，选中“对象实例”中的两个实例，选中 “指标名称”中的 “主备节点间同步率”，光标悬浮至下方的曲线图上，确认其当前同步率为 99.0 或者 100.0，则表示GaussDB服务数据同步完成。
            **图1** 业务监控

            <br>

            ![](节点重建（REB NODE）_71765323.assets/zh-cn_image_0000001415989264_2.png "点击放大")
    3. 确认Modulekeeper适配包同步完成。
          a. 使用**mtuser**用户通过“putty.exe”登录OMU，执行命令：**su root**
          b. 进入 /opt/container/log/0/Modulekeeper/ 目录。
          c. 执行如下命令，搜索适配包同步完成日志。
            **zgrep "recover adapter success, break" ***
          d. 若出现"recover adapter success, break"日志则说明适配包同步完成。
    4. 确认FileServer文件同步完成。
          a. 使用**mtuser**用户通过“putty.exe”登录OMU，执行命令：**su root**
          b. 进入cd /opt/container/log/0/FileServer目录。
          c. 执行如下命令，搜索文件同步完成日志。
            **zgrep "finish to sync file" ***
          d. 若出现"finish to sync file"日志则说明文件同步完成。
    5. 确认备份包文件同步完成。
          a. 使用**mtuser**用户通过“putty.exe”登录OMU，执行命令：**su root**
          b. 进入cd /opt/container/log/0/cspbackupmgr目录。
          c. 执行如下命令，搜索文件同步完成日志。
            **zgrep "innerMsgMgr.cleanOtherPeerPackage resp is" ***
          d. 若出现"errorcode":0,"errmsg":"successful"日志则说明文件同步完成。
    6. 重建下一个OMU节点。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| APPID | 网元ID | 可选必选说明：必选参数<br>参数含义：用于指示系统需要重建指定网元ID下的节点数据。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：<br>“网元ID”<br>获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。 |
| NODENAME | 节点名称 | 可选必选说明：必选参数<br>参数含义：用于指示系统需要重建哪个节点的数据。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：操作员可以使用<br>[**DSP NODE**](节点查询（DSP NODE）_71678755.md)<br>命令查询获得。 |
| REBUILDTYPE | 重装类型 | 可选必选说明：必选参数<br>参数含义：标识指定网元ID和指定节点重装重建的方式。<br>取值范围：<br>- “rebuildOS（重装OS）”<br>：会更换掉VM的系统盘，可能会导致数据盘数据丢失，需要按照资料严格操作，同时重新纳管时需要对数据盘进行重新挂载及数据保留。<br>- “rebuildVM（重建VM）”<br>：不改变节点的网络和存储，操作完成后业务继续运行，可能会导致数据盘数据丢失，需要按照资料严格操作。<br>默认值：无。<br>配置原则：优先使用<br>“rebuildVM（重建VM）”<br>恢复，如果<br>“rebuildVM（重建VM）”<br>无效则使用<br>“rebuildOS（重装OS）”<br>恢复。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NODE]] · 节点信息（NODE）

## 使用实例

重建节点： “网元ID” 为“0”， “节点名称” 为“10.0.0.1”， “重建类型” 为“重装OS”。

```
%%REB NODE: APPID=0, NODENAME="10.0.0.1", REBUILDTYPE=rebuildOS;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------
    状态  =  Success 
详细信息  =  操作成功 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/REB-NODE.md`
