---
id: UDG@20.15.2@MMLCommand@DSP IKEIPSECSTAT
type: MMLCommand
name: DSP IKEIPSECSTAT（显示IKE IPsec统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IKEIPSECSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- IKE统计信息
status: active
---

# DSP IKEIPSECSTAT（显示IKE IPsec统计信息）

## 功能

该命令用于显示IKE IPsec统计信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数表示Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IKE IPsec统计信息（IKEIPSECSTAT）](configobject/UDG/20.15.2/IKEIPSECSTAT.md)

## 使用实例

显示IKE IPsec统计信息

```
DSP IKEIPSECSTAT:;
RETCODE = 0  操作成功

结果如下
-------------------------
                                 Pod名称  =   ipsecexec-pod-0192-168-1-1
                  SA首次建立的AH或ESP数目  =  1
                  SA首次建立的AH和ESP数目  =  0
 重新申请密钥或重认证后SA更新的AH或ESP数目  =  3
 重新申请密钥或重认证后SA更新的AH和ESP数目  =  0
                           第一次软过期数  =  0
                           第二次软过期数  =  0
                           第三次软过期数  =  0
                                 硬过期数  =  0
                               删掉的SA数  =  8
                             删掉的新SA数  =  0
                       一秒内删掉的旧SA数  =  0
                       一秒后删掉的旧SA数  =  6
           保留的入IPSec隧道描述字模块数目  =  0
                       到达的入DHCP包数目  =  0
                       到达的出DHCP包数目  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IKE-IPsec统计信息（DSP-IKEIPSECSTAT）_97874058.md`
