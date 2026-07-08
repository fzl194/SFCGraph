---
id: UDG@20.15.2@MMLCommand@LST DETECTPATH
type: MMLCommand
name: LST DETECTPATH（查询探测路径配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DETECTPATH
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 路径管理
- N6路径管理
- N6路径参数
status: active
---

# LST DETECTPATH（查询探测路径配置）

## 功能

**适用NF：UPF**

![](查询探测路径配置（LST DETECTPATH）_44662158.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，否

该命令用于查询指定探测路径或者已配置的所有探测路径的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATHNAME | 路径名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用于连通性探测的路径名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DETECTPATH]] · 探测路径配置（DETECTPATH）

## 使用实例

查询当前已经配置的所有探测路径配置：

```
LST DETECTPATH:;
```

```

RETCODE = 0  操作成功

探测路径配置信息
----------------
路径名称   本端逻辑接口名称  对端IPV4地址  对端IPV6地址  发送GTP心跳请求的间隔时间  等待Echo响应超时时间  故障恢复阈值  故障阈值  探测路径状态  是否绑定APN  注册异步Ping任务  上次更新时间  

testpath3  phif1/0/1         0.0.0.0       FC00::        1                          2                     10            20        未使用        不使能       不使能            NULL          
testpath1  phif1/0/0         10.8.1.13     ::            1                          2                     10            20        未使用        不使能       不使能            NULL          
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DETECTPATH.md`
