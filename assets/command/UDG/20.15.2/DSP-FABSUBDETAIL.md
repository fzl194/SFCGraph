---
id: UDG@20.15.2@MMLCommand@DSP FABSUBDETAIL
type: MMLCommand
name: DSP FABSUBDETAIL（显示Fabric亚健康通信质量信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FABSUBDETAIL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP FABSUBDETAIL（显示Fabric亚健康通信质量信息）

## 功能

该命令用于显示Fabric亚健康通信质量信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAENODE**](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)<br>查看工作角色为数据转发对应的微服务实例号。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FABSUBDETAIL]] · Fabric亚健康通信质量信息（FABSUBDETAIL）

## 使用实例

查询Fabric亚健康通信质量。

```
%%DSP FABSUBDETAIL: CELLINSTANCE="sfpod-0__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
源Cell名称          源节点名称       源主机名称               目的Cell名称                            目的节点名称  目的主机名称            平面组ID  平面ID  亚健康发生时间
sfpod-0__103__0     192.168.1.1      vlab19-dc15-sr6-s1ot11   srvcssim-pod-847c759984-k44qz__103__0   192.168.1.2   vlab19-dc15-sr6-s1ot15  200       101     2024-12-05 23:35:09
sfpod-0__103__0     192.168.1.1      vlab19-dc15-sr6-s1ot11   vsm-pod-7b88bdc974-spk84__103__0        192.168.1.2   vlab19-dc15-sr6-s1ot15  100       100     2024-12-05 23:35:09
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FABSUBDETAIL.md`
