---
id: UNC@20.15.2@MMLCommand@DSP DIFFSERVICE
type: MMLCommand
name: DSP DIFFSERVICE（显示差异化服务信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DIFFSERVICE
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 差异化服务配置
status: active
---

# DSP DIFFSERVICE（显示差异化服务信息）

## 功能

**适用网元：SGSN**

该命令用于查询系统运行过程中差异化服务信息，包括系统中正在运行的不同用户级别用户个数和不同用户级别业务级别的用户差异服务用户接入和PDP接入的情况。

## 注意事项

如果输入RU名称和进程号，就查询这个SPP进程上的当前的差异化服务信息；如果没有输入RU名称和进程号，则查询系统所有的差异化服务的信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：1～63位字符串<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于显示业务进程所属的SPP进程序号。<br>数据来源：本端规划<br>取值范围：0～20<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DIFFSERVICE]] · 差异化服务接入门限（DIFFSERVICE）

## 使用实例

查询整系统差异化服务信息：

DSP DIFFSERVICE:;

```
%%DSP DIFFSERVICE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
2G 高端用户 = 0
2G 普通用户 = 0
2G 低端用户 = 0
3G 高端用户 = 0
3G 普通用户 = 0
3G 低端用户 = 0
仍有后续报告输出
---    END

%%DSP DIFFSERVICE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
用户级别     2G用户接入     3G用户接入

高端用户     允许接入       允许接入
普通用户     允许接入       允许接入
低端用户     允许接入       允许接入 
仍有后续报告输出
---    END

%%DSP DIFFSERVICE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
用户级别     业务级别                   2G PDP接入     3G PDP接入
                                                   
高端用户     Conversation               允许接入       允许接入
高端用户     StreamingGBRMore25Kbps     允许接入       允许接入
高端用户     StreamingGBRLess24Kbps     允许接入       允许接入
高端用户     InteractiveTrafficPri1     允许接入       允许接入
高端用户     InteractiveTrafficPri2     允许接入       允许接入
高端用户     InteractiveTrafficPri3     允许接入       允许接入
高端用户     Background                 允许接入       允许接入
普通用户     Conversation               允许接入       允许接入
普通用户     StreamingGBRMore25Kbps     允许接入       允许接入
普通用户     StreamingGBRLess24Kbps     允许接入       允许接入
普通用户     InteractiveTrafficPri1     允许接入       允许接入
普通用户     InteractiveTrafficPri2     允许接入       允许接入
普通用户     InteractiveTrafficPri3     允许接入       允许接入
普通用户     Background                 允许接入       允许接入
低端用户     Conversation               允许接入       允许接入
低端用户     StreamingGBRMore25Kbps     允许接入       允许接入
低端用户     StreamingGBRLess24Kbps     允许接入       允许接入
低端用户     InteractiveTrafficPri1     允许接入       允许接入
低端用户     InteractiveTrafficPri2     允许接入       允许接入
低端用户     InteractiveTrafficPri3     允许接入       允许接入
低端用户     Background                 允许接入       允许接入
(结果个数 = 25)
共有3个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DIFFSERVICE.md`
