---
id: UNC@20.15.2@MMLCommand@DSP PRTGRPINFO
type: MMLCommand
name: DSP PRTGRPINFO（显示保护组信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PRTGRPINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 保护组管理
status: active
---

# DSP PRTGRPINFO（显示保护组信息）

## 功能

该命令用于显示保护组信息。

外部网关路由器只与保护组内ISU/APU之间建立BFD会话，备路由也只到保护组内ISU/APU的ECMP路由。

## 注意事项

- 此命令仅在虚机场景下支持。
- 仅ISU/APU场景支持显示保护组信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PRTGRPINFO]] · 保护组信息（PRTGRPINFO）

## 使用实例

假如运营商想要查看哪些VNRS RU处于保护组中，调用以下命令可以看到所有处于保护组中的VNRS RU信息。

```
%%DSP PRTGRPINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
RuId  RuName           PodName    VmId                              VmName                      

64    VNRS_IP_RU_0064  isu-pod-0  cef65e1bbe3045279fee856349d7b84b  env198_UDG_VNF_1109_ISU__1  
65    VNRS_IP_RU_0065  isu-pod-1  b04ad5c5aadc4e7a9d8f67a3d86bc906  env198_UDG_VNF_1109_ISU__0  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PRTGRPINFO.md`
