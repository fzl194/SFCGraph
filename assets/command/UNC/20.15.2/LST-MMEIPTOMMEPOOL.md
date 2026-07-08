---
id: UNC@20.15.2@MMLCommand@LST MMEIPTOMMEPOOL
type: MMLCommand
name: LST MMEIPTOMMEPOOL（查询MME IP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMEIPTOMMEPOOL
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- MME IP
status: active
---

# LST MMEIPTOMMEPOOL（查询MME IP）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于显示MME POOL绑定的地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 参数含义：该参数用于指定MME POOL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD MMEPOOL命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEIPTOMMEPOOL]] · MME IP（MMEIPTOMMEPOOL）

## 使用实例

假设用户需要查询名为“mmepool1”的MME POOL：

```
%%LST MMEIPTOMMEPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
		     MME POOL名称  =  mmepool1
				   IP版本  =  IPV4
		    MME的IPv4地址  =  10.0.0.10
		    MME的IPv6地址  =  ::
		  是否为备份的MME  =  否
				     端口  =  2123
		   MME IP描述信息  =  NULL
备份的MME优先使用的IP版本  =  NULL

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MMEIPTOMMEPOOL.md`
