---
id: UNC@20.15.2@MMLCommand@DSP TRCTASKSTC
type: MMLCommand
name: DSP TRCTASKSTC（显示跟踪任务相关跟踪消息的统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TRCTASKSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 跟踪管理调测
status: active
---

# DSP TRCTASKSTC（显示跟踪任务相关跟踪消息的统计信息）

## 功能

该命令用于显示跟踪任务相关跟踪消息的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPONENTID | 组件ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定组件ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：必须是订阅处理跟踪业务的组件ID。 |
| TRACETASKID | 跟踪任务号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示跟踪任务号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TRCTASKSTC]] · 跟踪任务相关跟踪消息的统计信息（TRCTASKSTC）

## 使用实例

显示跟踪任务相关跟踪消息的统计信息，可通过如下命令显示：

```
DSP TRCTASKSTC:COMPONENTID=2161312903,TRACETASKID=10
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
                        跟踪任务号  =  10
                      跟踪业务类型  =  120
                        接收消息数  =  0
              任务未激活丢弃消息数  =  0
          组合条件不匹配丢弃消息数  =  0
          过滤条件不匹配丢弃消息数  =  0
                缓冲区满丢弃消息数  =  0
实时流控方式下报数超阈值丢弃消息数  =  0
        跟踪发送模式非法丢弃消息数  =  0
            申请消息失败丢弃消息数  =  0
              重定向失败丢弃消息数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TRCTASKSTC.md`
