# 查询全局缺省PCRF组（LST DFTGLBPCRFGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897114__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897114__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897114__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897114__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897114__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897114__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897114)

**适用NF：PGW-C、GGSN**

此命令用来查询缺省全局PCRF分组。

#### [注意事项](#ZH-CN_CONCEPT_0209897114)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897114)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897114)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209897114)

显示DFTGLBPCRFGRP：

```
LST DFTGLBPCRFGRP:;
```

```

RETCODE = 0  操作成功。

全局缺省PCRF组
--------------
PCRF组名称  =  pcr
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897114)

参见SET DFTGLBPCRFGRP的参数说明。
