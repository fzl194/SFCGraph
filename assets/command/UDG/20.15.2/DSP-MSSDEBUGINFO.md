---
id: UDG@20.15.2@MMLCommand@DSP MSSDEBUGINFO
type: MMLCommand
name: DSP MSSDEBUGINFO（查询维测开关状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSDEBUGINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 维测开关统计查询
status: active
---

# DSP MSSDEBUGINFO（查询维测开关状态）

## 功能

该命令用于查询维测开关状态信息。

维测开关包括调度、保序和定时器维测开关，默认是关闭的。

例如，当需要定位调度线程是否异常切换，打开调度轨迹开关后通过查询维测命令查看开关是否打开。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSDEBUGINFO]] · 维测开关状态（MSSDEBUGINFO）

## 使用实例

查询维测开关信息：

```
DSP MSSDEBUGINFO:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
    调度组维测状态 / 剩余时间（s）  =  OFF
  调度队列维测状态 / 剩余时间（s）  =  OFF
      Work维测状态 / 剩余时间（s）  =  OFF
      节能维测状态 / 剩余时间（s）  =  OFF
  调度轨迹维测状态 / 剩余时间（s）  =  OFF
  保序队列维测状态 / 剩余时间（s）  =  OFF
  保序精度维测状态 / 剩余时间（s）  =  OFF
定时器事件维测状态 / 剩余时间（s）  =  OFF
定时器精度维测状态 / 剩余时间（s）  =  OFF
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSDEBUGINFO.md`
