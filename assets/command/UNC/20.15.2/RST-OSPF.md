---
id: UNC@20.15.2@MMLCommand@RST OSPF
type: MMLCommand
name: RST OSPF（重置OSPF进程）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: OSPF
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 重置OSPF进程
status: active
---

# RST OSPF（重置OSPF进程）

## 功能

![](重置OSPF进程（RST OSPF）_49802458.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致路由器之间的OSPF邻接关系中断，且以前的信息将无法恢复，请谨慎使用并联系华为技术支持协助操作。

该命令用于重置OSPF进程。

## 注意事项

- 该命令执行后立即生效。
- 重置OSPF进程可能会导致业务受损。
- 只有在配置了OSPF进程后才能使用此命令。
- 复位OSPF进程会导致路由器之间的OSPF邻接关系中断，且以前的信息将无法恢复。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：如果不输入该参数，则表示匹配所有OSPF进程。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPF]] · OSPF进程配置（OSPF）

## 使用实例

重置所有进程号为1的OSPF进程：

```
RST OSPF: PROCID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RST-OSPF.md`
