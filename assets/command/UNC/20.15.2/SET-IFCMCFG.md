---
id: UNC@20.15.2@MMLCommand@SET IFCMCFG
type: MMLCommand
name: SET IFCMCFG（设置IFCM配置信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IFCMCFG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- IFCM管理
status: active
---

# SET IFCMCFG（设置IFCM配置信息）

## 功能

![](设置IFCM配置信息(SET IFCMCFG)_67652254.assets/notice_3.0-zh-cn_2.png)

**执行该命令会改变IFCM系统配置，对故障诊断恢复结果造成影响，请慎重执行。**

该命令用于设置IDRService配置信息。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：指定要设置哪个网元的配置信息。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| CFG_TYPE | 配置名称 | 可选必选说明：必选参数。<br>参数含义：指定要配置项。<br>取值范围：<br>- “byME(网元故障阈值)”：配置网元级故障阈值。<br>- “byPod(Pod故障阈值)”：配置Pod级的故障阈值。<br>- “byPool(网元容灾阈值)”：配置网元级的容灾倒换阈值。<br>默认值：无。<br>配置原则：无。 |
| THRESHOLD | 配置阈值(%) | 可选必选说明：必选参数。<br>参数含义：发送给服务的阈值信息。<br>取值范围：整数类型，当<br>“配置名称”<br>为<br>“byME(网元故障阈值)”<br>和<br>“byPod(Pod故障阈值)”<br>时取值范围为1~100，当<br>“配置名称”<br>为<br>“byPool(网元容灾阈值)”<br>时取值范围为5~100。<br>“byME(网元故障阈值)”<br>必须严格小于<br>“byPool(网元容灾阈值)”<br>。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFCMCFG]] · IFCM配置信息（IFCMCFG）

## 使用实例

设置网元容灾倒换阈值：

```
%%SET IFCMCFG: MEID=0, CFG_TYPE=byPool, THRESHOLD=18;%%
RETCODE = 0  操作成功
操作结果如下： 
-------------- 
操作结果  =  success 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IFCMCFG.md`
