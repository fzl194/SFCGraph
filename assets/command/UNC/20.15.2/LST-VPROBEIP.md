---
id: UNC@20.15.2@MMLCommand@LST VPROBEIP
type: MMLCommand
name: LST VPROBEIP（查询vProbe报表本地IP资源池）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VPROBEIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- vProbe管理
- vProbe本地IP
status: active
---

# LST VPROBEIP（查询vProbe报表本地IP资源池）

## 功能

该命令用于查询vProbe的报表本地IP资源池。

## 注意事项

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPROBEIP]] · vProbe报表本地IP资源池（VPROBEIP）

## 使用实例

运营商A查询vProbe配置单据上报的本地IP资源池配置信息：

```
%%LST VPROBEIP:;%%
RETCODE = 0  操作成功

结果如下
--------
    索引号  =  1
  协议类型  =  TCP
    IP类型  =  IPv4
  IPv4地址  =  10.185.23.253
  IPv6地址  =  ::
起始端口号  =  6000
结束端口号  =  6002
   VPN名称  =  _public_
      描述  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VPROBEIP.md`
