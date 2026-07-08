---
id: UDG@20.15.2@MMLCommand@DSP ECOVMSINFO
type: MMLCommand
name: DSP ECOVMSINFO（显示VM的CPU节能策略）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ECOVMSINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- CPU节能策略
status: active
---

# DSP ECOVMSINFO（显示VM的CPU节能策略）

## 功能

该命令用于在开启节能策略后，查询当前VM的CPU节能策略。

> **说明**
> - 此命令仅在虚机场景下支持。
> - 部分场景下，VM实际节能策略可能与网元期望策略不同，此时，最长需要24小时可自动刷新为期望策略。此时，可通过执行[**SET ECOPOLICY**](设置全局的CPU调频和休眠策略（SET ECOPOLICY）_97016349.md)命令先关闭、再开启节能功能，使VM实际节能策略快速恢复（约2分钟）。
>
> - VNF更新操作会将网元所有VM的实际节能策略恢复为VNFD模板定义的初始节能策略。
> - VM重建、对没有部署Pod的VM进行上下电操作，会将该VM的实际节能策略恢复为VNFD模板定义的初始节能策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ECOVMSINFO]] · VM的CPU节能策略（ECOVMSINFO）

## 使用实例

查询VM节能策略：

```
%%DSP ECOVMSINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
VM名称                   策略同步是否一致  CPU休眠策略期望值  CPU休眠策略实际值  CPU调频策略期望值  CPU调频策略实际值  

project-env106_EXU__0    是                深休眠             深休眠             开启               开启               
project-env106_IPU__0    是                深休眠             深休眠             不支持             不支持             
project-env106_IPU__1    是                深休眠             深休眠             不支持             不支持             
project-env106_OMU__0    是                不支持             不支持             开启               开启               
project-env106_OMU__1    是                不支持             不支持             开启               开启               
project-env106_SDU__0    是                深休眠             深休眠             开启               开启               
project-env106_SDU__1    是                深休眠             深休眠             开启               开启               
project-env106_SGU_A__0  是                深休眠             深休眠             开启               开启               
project-env106_SGU_A__1  是                深休眠             深休眠             开启               开启               
project-env106_SGU_S__0  是                深休眠             深休眠             开启               开启               
project-env106_SGU_S__1  是                深休眠             深休眠             开启               开启               
project-env106_UPU__0    是                深休眠             深休眠             开启               开启               
project-env106_UPU__1    是                深休眠             深休眠             开启               开启               
(结果个数 = 13)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ECOVMSINFO.md`
