---
id: UNC@20.15.2@MMLCommand@DSP CHGCG
type: MMLCommand
name: DSP CHGCG（显示CG状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CHGCG
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# DSP CHGCG（显示CG状态）

## 功能

**适用网元：SGSN**

该命令用于查询对端CG与本端SGSN的通信状态。

## 注意事项

- 该命令执行后立即生效。
- 如果输入的RU名称中不存在，将会提示没有满足条件的记录

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的资源单元名称。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划<br>取值范围：0 ~ 63位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGCG]] · CG配置参数（CHGCG）

## 使用实例

查询CDP进程对应的所有CG状态：

DSP CHGCG:;

```
%%DSP CHGCG:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
RU名称            进程号    CG的IP地址      CG状态      GTP承载协议    CG接收端口号
      
USN_SP_RU_0067    0         192.168.253.1   通信正常    UDP            4007        
USN_SP_RU_0066    0         192.168.253.1   通信正常    UDP            4007       
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CHGCG.md`
