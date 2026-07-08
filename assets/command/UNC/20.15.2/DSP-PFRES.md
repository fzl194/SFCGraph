---
id: UNC@20.15.2@MMLCommand@DSP PFRES
type: MMLCommand
name: DSP PFRES（显示带宽资源使用明细）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PFRES
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- 转发资源管理
- 带宽资源管理
- 带宽资源参数管理
status: active
---

# DSP PFRES（显示带宽资源使用明细）

## 功能

**适用网元：SGSN**

该命令用于查看各个节点上的资源使用情况。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>**DSP RU**<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPP进程的序号。<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [带宽资源使用明细（PFRES）](configobject/UNC/20.15.2/PFRES.md)

## 使用实例

查询资源单元为USN_SP_RU_0066上0号UPP进程的资源使用情况：

DSP PFRES: RUNAME="USN_SP_RU_0066", PN=0;

```
%%DSP PFRES: RUNAME="USN_SP_RU_0066", PN=0;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
                           RU名称  =  USN_SP_RU_0066
               	           进程号  =  0
             用户面总带宽(kbit/s)  =  4000000
   预防突发流量的预留带宽(kbit/s)  =  40000
           总静态使用带宽(kbit/s)  =  0
           总动态使用带宽(kbit/s)  =  0
       QOS1类业务静态带宽(kbit/s)  =  0
       QOS2类业务静态带宽(kbit/s)  =  0
      QOS12类业务动态带宽(kbit/s)  =  0
       QOS3类业务动态带宽(kbit/s)  =  0
       QOS4类业务动态带宽(kbit/s)  =  0
 目的地址非本板的转发带宽(kbit/s)  =  0
                 QOS1类业务用户数  =  0
                 QOS2类业务用户数  =  0
                 QOS3类业务用户数  =  0
                 QOS4类业务用户数  =  0
                        PDP数状态  =  正常
                       Path数状态  =  正常
            包转发速率(Packets/s)  =  19
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示带宽资源使用明细(DSP-PFRES)_26145850.md`
