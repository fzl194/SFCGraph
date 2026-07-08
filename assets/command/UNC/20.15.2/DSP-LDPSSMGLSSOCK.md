---
id: UNC@20.15.2@MMLCommand@DSP LDPSSMGLSSOCK
type: MMLCommand
name: DSP LDPSSMGLSSOCK（显示LDP的Listen Socket信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPSSMGLSSOCK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPSSMGLSSOCK（显示LDP的Listen Socket信息）

## 功能

该命令用于显示LDP的Listen Socket信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPSSMGLSSOCK]] · LDP的Listen Socket信息（LDPSSMGLSSOCK）

## 使用实例

显示LDP的Listen Socket信息：

```
DSP LDPSSMGLSSOCK:VRFNAME="_public_";
```

```

RETCODE = 0  操作成功。

结果如下
--------
            VPN实例名称  =  _public_
         对等体的LSR ID  =  10.10.10.10
  LDP分配给Socket的编号  =  12
  Socket分配给LDP的编号  =  12
    LDP TCP连接的源地址  =  10.10.10.3
  LDP TCP连接的目的地址  =  10.10.10.10
   TCP Socket创建的状态  =  Socket创建成功
           KeyChain状态  =  未设置Socket选项
                MD5状态  =  未设置Socket选项
               GTSM状态  =  未设置Socket选项
       Socket的备份状态  =  空闲状态
       Socket的备份类型  =  备份类型无效
       Socket备份版本号  =  0
LDP分布式整数形式的编号  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示LDP的Listen-Socket信息（DSP-LDPSSMGLSSOCK）_00440549.md`
