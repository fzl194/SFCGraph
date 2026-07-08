---
id: UDG@20.15.2@MMLCommand@SET OMSWITCH
type: MMLCommand
name: SET OMSWITCH（设置OM功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: OMSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# SET OMSWITCH（设置OM功能开关）

## 功能

![](设置OM功能开关（SET OMSWITCH）_86362910.assets/notice_3.0-zh-cn.png)

执行该命令关闭功能开关时会导致 OM Portal 不可用，影响OM网络运维通道，请谨慎操作。

此命令用于设置OM功能开关的开关状态。

> **说明**
> - 关闭Portal功能开关会导致OM Portal不可用，无法通过OM Portal进行运维。
> - 该命令为二次授权命令，执行该命令前请先收集二次授权的账户和密码。
> - 关闭Portal功能开关会导致31943端口关闭，周边部件依赖该通道的功能不可用，如：
>     - LCM
>           - VNF更新
>           - VNF扩缩容
>           - VNF自愈
>           - VNF卸载
>     - 网管
>           - 网元信息采集
>           - 创建网元跟踪任务
>           - 同步、上传、激活、删除、下载网元license文件
>           - 网元备份
>           - 维护台跳转网元
>           - 网元证书激活、回退、导入
>           - syslog对接网元
>           - 网元MML配置导出下载
>           - 网元升级
>           - 网元话单查询和下载
>     - 4A对接
> - 关闭Portal功能开关后，如需开启，需要在网管界面执行此MML命令开启。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| FUNC | 功能 | 可选必选说明：必选参数。<br>参数含义：功能。<br>取值范围：PORTAL(Portal)<br>默认值：PORTAL(Portal)。<br>配置原则：无。 |
| SWITCH | 开关 | 可选必选说明：必选参数。<br>参数含义：功能开关。<br>取值范围：<br>- ON(开)<br>- OFF(关)<br>默认值：ON(开)。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OMSWITCH]] · OM功能开关（OMSWITCH）

## 使用实例

设置OM功能开关：

```
%%SET OMSWITCH: FUNC=PORTAL, SWITCH=OFF;%% 
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-OMSWITCH.md`
