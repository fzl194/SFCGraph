---
id: UNC@20.15.2@MMLCommand@LST SDRTRANS
type: MMLCommand
name: LST SDRTRANS（查询SDR传输能力）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SDRTRANS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 传输能力控制
status: active
---

# LST SDRTRANS（查询SDR传输能力）

## 功能

该命令用于查询SDR传输能力。

## 注意事项

无

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLATTYPE | 通信平面类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR通信平面类型。<br>数据来源：本端规划<br>取值范围：<br>- “BASE（Base）”：Base平面<br>- “FABRIC（Fabric）”：Fabric平面<br>默认值：无<br>配置原则：无 |
| TRANSABILITY | 传输能力类型 | 可选必选说明：可选参数<br>参数含义：该参数用于标识SDR传输能力类型。<br>数据来源：本端规划<br>取值范围：<br>- “RELIABILITY（可靠传输能力）”：可靠传输能力<br>- “SECURITY（安全传输能力）”：安全传输能力<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRTRANS]] · SDR传输能力（SDRTRANS）

## 使用实例

查询SDR的BASE平面RELIABILITY传输能力：

```
%%LST SDRTRANS: FLATTYPE=BASE, TRANSABILITY=RELIABILITY;%%
RETCODE = 0  操作成功

结果如下
--------
通信平面类型  =  Base
传输能力类型  =  可靠传输能力
    选项开关  =  不设置该传输能力
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SDRTRANS.md`
