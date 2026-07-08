---
id: UNC@20.15.2@MMLCommand@RST MESYS
type: MMLCommand
name: RST MESYS（复位网元服务）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: MESYS
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 网元管理
status: active
---

# RST MESYS（复位网元服务）

## 功能

![](复位网元服务（RST MESYS）_72247081.assets/notice_3.0-zh-cn_2.png)

- 复位网元服务可能导致业务呼损，请确认是否继续操作。
- 三方CaaS场景该命令依赖LCM配套版本，其它场景无此限制。
- 该命令属于“网元ID”为“0”下的业务，参数“网元ID”输入“0”时重建Pod为异步操作，命令返回操作成功后1-3min刷新页面失败可判断重建Pod成功，反之则失败；参数“网元ID”输入非“0”时重建Pod为同步操作。

本命令用于对指定的网元进行复位。RST MESYS会将指定网元下的POD全部重建。

## 注意事项

RST MESYS存在异步操作，实际复位结果可能存在一定时间的延迟。

复位 “网元ID” 为 “0” 的网元可能会导致无法在MML页面上查看到操作结果报文。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：复位的网元ID，即应用ID（可以通过MML命令“<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>”获取）。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MESYS]] · 复位网元服务（MESYS）

## 使用实例

根据网元ID复位。

```
%%RST MESYS: MEID=0;%% 
RETCODE = 0 操作成功
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/复位网元服务（RST-MESYS）_72247081.md`
