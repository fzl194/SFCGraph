---
id: UDG@20.15.2@MMLCommand@RST NODEBATCH
type: MMLCommand
name: RST NODEBATCH（节点批量复位）
nf: UDG
version: 20.15.2
verb: RST
object_keyword: NODEBATCH
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# RST NODEBATCH（节点批量复位）

## 功能

![](节点批量复位（RST NODEBATCH）_73743460.assets/notice_3.0-zh-cn.png)

- 执行该命令会批量复位指定网元ID下的所有非Stopped状态的节点，影响节点上的业务，请慎重使用该命令。
- 在存储故障期间，执行该命令批量复位节点后，这些节点以及节点中的容器和进程，在存储恢复前都无法启动。
- 在扩容后30min内进行批量复位，存在不对扩容节点复位的问题，当出现此情况时，请执行**[RST NODE](节点复位（RST NODE）_71765322.md)**对未复位的节点进行复位。
- 在缩容后30min内进行批量复位，存在批量复位不生效或者失败的问题，当出现此情况时，请在缩容30min后再次进行批量复位操作，或者通过**[DSP NODE](节点查询（DSP NODE）_71678755.md)**查询节点信息，通过**[RST NODE](节点复位（RST NODE）_71765322.md)**对未复位的节点进行复位。
- 执行该命令批量复位节点后会重新加载适配包资源。复位前未关闭MML前台界面，可能会影响MML适配包加载，导致MML命令执行失败，此时需要清理浏览器缓存，再刷新界面即可正常执行MML命令。

本命令用于复位指定网元ID下的所有节点。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| APPID | 网元ID | 可选必选说明：必选参数<br>参数含义：用于指示系统需要批量复位指定网元ID下的节点数据。获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NODEBATCH]] · 节点批量复位（NODEBATCH）

## 使用实例

批量复位 “网元ID” 为“0”的节点。

```
%%RST NODEBATCH: APPID=0;%% 
RETCODE = 0  操作成功  

    状态  =  Success 
详细信息  =  操作成功
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/节点批量复位（RST-NODEBATCH）_73743460.md`
