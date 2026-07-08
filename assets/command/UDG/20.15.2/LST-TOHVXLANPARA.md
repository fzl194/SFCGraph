---
id: UDG@20.15.2@MMLCommand@LST TOHVXLANPARA
type: MMLCommand
name: LST TOHVXLANPARA（查询家庭网关业务使用VXLAN隧道传输业务参数配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOHVXLANPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- 家庭网关VXLAN隧道参数
status: active
---

# LST TOHVXLANPARA（查询家庭网关业务使用VXLAN隧道传输业务参数配置）

## 功能

**适用NF：UPF**

该命令用于查询家庭网关业务使用VXLAN隧道传输业务参数配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOHVXLANPARA]] · 家庭网关业务使用VXLAN隧道传输业务参数配置（TOHVXLANPARA）

## 使用实例

显示VXLAN隧道传输业务参数配置：

```
LST TOHVXLANPARA:;
```

```

RETCODE = 0  操作成功

结果如下
--------
         VXLAN隧道开关  =  使能
       VXLAN隧道源接口  =  NULL
  VXLAN隧道源端MAC地址  =  28-6E-D4-89-91-40
      虚拟网关IPv4地址  =  192.168.123.166
 免费ARP发送定时器时长  =  270
          心跳检测开关  =  不使能
        时间阈值（秒）  =  6
      心跳检测成功次数  =  3
      心跳检测失败次数  =  3
Ping探测超时时长（秒）  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询家庭网关业务使用VXLAN隧道传输业务参数配置（LST-TOHVXLANPARA）_29481111.md`
