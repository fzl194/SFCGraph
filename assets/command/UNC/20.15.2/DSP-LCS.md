---
id: UNC@20.15.2@MMLCommand@DSP LCS
type: MMLCommand
name: DSP LCS（查询LCS资源状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LCS
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS操作维护
status: active
---

# DSP LCS（查询LCS资源状态）

## 功能

**适用网元：SGSN、MME**

该命令用于查询LCS的资源状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查询的SPP进程的进程号。<br>数据来源：整网规划。<br>取值范围：0~20<br>默认值：无<br>说明：输入该参数时必须输入<br>“RU名称”<br>参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LCS]] · LCS资源状态（LCS）

## 使用实例

查询LCS控制表的占用情况：

DSP LCS: RUNAME="USN_SP_RU_0064", PROCNO=0;

```
%%DSP LCS: RUNAME="USN_SP_RU_0064", PROCNO=0;%%
RETCODE = 0  操作成功。

输出结果如下
------------
          RU名称 = USN_SP_RU_0064
          进程号 = 0
     LCS资源总量 = 500
   LCS资源使用量 = 0
  4G LCS资源总量 = 800
4G LCS资源使用量 = 0
 (结果个数 = 1)
 
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LCS资源状态(DSP-LCS)_72345417.md`
