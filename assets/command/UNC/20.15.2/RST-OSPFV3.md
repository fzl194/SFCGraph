---
id: UNC@20.15.2@MMLCommand@RST OSPFV3
type: MMLCommand
name: RST OSPFV3（重置OSPFv3进程）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: OSPFV3
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 重置OSPFv3进程
status: active
---

# RST OSPFV3（重置OSPFv3进程）

## 功能

![](重置OSPFv3进程（RST OSPFV3）_00601085.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致路由器之间的OSPFv3邻接关系中断，且以前的信息将无法恢复，请谨慎使用并联系华为技术支持协助操作。

该命令用于重置OSPFv3进程。

## 注意事项

- 该命令执行后立即生效。
- 重置OSPFv3进程可能会导致业务受损。
- 只有在配置了OSPFv3进程后才能使用此命令。
- 复位OSPFv3的连接会导致路由器之间的OSPFv3邻接关系中断，且以前的信息将无法恢复。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：<br>- 必须重置已存在的OSPFv3进程。<br>- 如果不输入该参数，则表示匹配所有OSPFv3进程。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3]] · OSPFv3进程配置（OSPFV3）

## 使用实例

重启所有进程号为1的OSPFv3进程：

```
RST OSPFV3: PROCID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/重置OSPFv3进程（RST-OSPFV3）_00601085.md`
